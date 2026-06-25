import re


# =============================================================================
# SMART TOKENIZER
# Splits compound inputs into individual base words before any heuristic runs.
#   CamelCase  → "AhsanAhmad"       → ["ahsan", "ahmad"]
#   Comma sep  → "Coding,Volleyball" → ["coding", "volleyball"]
#   Spaces     → "New Delhi"         → ["new", "delhi"]
# =============================================================================
def tokenize(value):
    value = str(value).strip()
    spaced = re.sub(r'([a-z])([A-Z])', r'\1 \2', value)
    tokens = re.split(r'[\s,.\-_]+', spaced)
    return [t.lower() for t in tokens if t.strip()]


# =============================================================================
# LEET SPEAK MUTATIONS
# =============================================================================
LEET_MAP = {'a': '@', 'e': '3', 'i': '1', 'o': '0', 's': '$', 't': '7', 'l': '1'}

def leet(word):
    return ''.join(LEET_MAP.get(c, c) for c in word)

def leet_changed(word):
    return leet(word) != word


# =============================================================================
# LENGTH FILTER PARSER
# Parses user input like "8", "8-12", "8-16" into a (min, max) tuple.
# Returns (None, None) if input is empty or invalid — meaning no filter.
# =============================================================================
def parse_length_filter(length_input):
    if not length_input or not str(length_input).strip():
        return None, None
    raw = str(length_input).strip()
    # Range format: "8-12"
    range_match = re.match(r'^(\d+)\s*[-–]\s*(\d+)$', raw)
    if range_match:
        lo, hi = int(range_match.group(1)), int(range_match.group(2))
        return min(lo, hi), max(lo, hi)
    # Single number: "8"
    single_match = re.match(r'^(\d+)$', raw)
    if single_match:
        n = int(single_match.group(1))
        return n, n
    return None, None


# =============================================================================
# MAIN GENERATOR
# =============================================================================
def generate_heuristic_dict(data):
    """
    Smart heuristic password dictionary generator.
    Prioritises likely passwords over brute quantity.
    """

    # -------------------------------------------------------------------------
    # STEP 1: Collect & tokenize text fields — CamelCase/comma/space aware
    # -------------------------------------------------------------------------
    raw_word_fields = [
        data.get('firstName'), data.get('lastName'), data.get('partnerName'),
        data.get('petName'), data.get('companyCollege'), data.get('hometown'),
        data.get('color'), data.get('hobby')
    ]
    words = []
    for field in raw_word_fields:
        if field and str(field).strip():
            words.extend(tokenize(field))
    words = list(dict.fromkeys(words))  # deduplicate, preserve order

    # -------------------------------------------------------------------------
    # STEP 2: Collect numbers — str() cast prevents crash on integer birthYear
    # -------------------------------------------------------------------------
    raw_numbers = [data.get('birthYear'), data.get('importantDate')]
    user_numbers = [str(n).strip() for n in raw_numbers if n and str(n).strip()]

    # -------------------------------------------------------------------------
    # STEP 3: Process custom field safely
    # -------------------------------------------------------------------------
    custom_input = data.get('commonField') or ''
    symbols = ['@', '#', '!', '_', '$', '*', '.', '-']

    for item in [i.strip() for i in custom_input.split(',') if i.strip()]:
        if not item.isalnum():
            symbols.append(item)
        elif item.isdigit():
            user_numbers.append(item)
        else:
            words.extend(tokenize(item))
            user_numbers.append(item)

    symbols = list(set(symbols))

    # -------------------------------------------------------------------------
    # STEP 4: Number pools — user numbers tried first, then common suffixes
    # -------------------------------------------------------------------------
    common_numbers = ['123', '1234', '12345', '786', '007', '69', '1', '01',
                      '99', '2024', '2025', '2026', '000', '111', '321']
    all_numbers = list(dict.fromkeys(user_numbers + common_numbers))

    # -------------------------------------------------------------------------
    # STEP 5: Expand words with leet + reverse mutations
    # -------------------------------------------------------------------------
    expanded_words = list(words)
    for w in words:
        expanded_words.append(w[::-1])
        if leet_changed(w):
            expanded_words.append(leet(w))
    expanded_words = list(dict.fromkeys(expanded_words))

    # =========================================================================
    # HEURISTIC ENGINE — ordered most → least likely
    # =========================================================================
    dictionary = set()

    # H1: Base words alone
    for w in expanded_words:
        dictionary.add(w)

    # H2: Word + UserNumber / Number + Word
    for w in expanded_words:
        for n in user_numbers:
            dictionary.add(w + n)
            dictionary.add(n + w)

    # H3: Word + Symbol + UserNumber  ← where "Ahsan@145" lives
    for w in expanded_words:
        for n in user_numbers:
            for s in symbols:
                dictionary.add(w + s + n)
                dictionary.add(w + n + s)

    # H4: Word + CommonNumber
    for w in expanded_words:
        for n in common_numbers:
            dictionary.add(w + n)

    # H5: Word + Symbol + CommonNumber
    for w in expanded_words:
        for n in common_numbers:
            for s in symbols:
                dictionary.add(w + s + n)

    # H6: Word + Word / Word + Symbol + Word
    for i, w1 in enumerate(words):
        for j, w2 in enumerate(words):
            if i != j:
                dictionary.add(w1 + w2)
                for s in symbols:
                    dictionary.add(w1 + s + w2)

    # H7: Word + Word + UserNumber / Word + Word + Symbol + UserNumber
    for i, w1 in enumerate(words):
        for j, w2 in enumerate(words):
            if i != j:
                for n in user_numbers:
                    dictionary.add(w1 + w2 + n)
                    for s in symbols:
                        dictionary.add(w1 + w2 + s + n)

    # =========================================================================
    # CAPITALIZATION — lowercase + Capitalized + UPPER applied to everything
    # =========================================================================
    final_dict = set()
    for pwd in dictionary:
        final_dict.add(pwd)
        final_dict.add(pwd.capitalize())
        final_dict.add(pwd.upper())

    # =========================================================================
    # LENGTH FILTER — applied as the very last step
    # "8"    → keep only len == 8
    # "8-12" → keep only 8 <= len <= 12
    # empty  → no filter, return all
    # =========================================================================
    min_len, max_len = parse_length_filter(data.get('passwordLength'))
    if min_len is not None:
        final_dict = {p for p in final_dict if min_len <= len(p) <= max_len}

    return list(final_dict)