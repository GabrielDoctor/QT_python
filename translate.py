import trie
import text_process
vp_dict = trie.Trie()
name_dict = trie.Trie()
hv_map = {}
full_width_punctuation = {
        '，': ',', '。': '.', '！': '!', '？': '?', '：': ':', '；': ';',
        '“': '"', '”': '"', '（': '(', '）': ')', '【': '[', '】': ']',
        '《': '<', '》': '>', '〈': '<', '〉': '>', '、': ',', '『': '"', '』': '"',
    }

class Token:
    def __init__(self, key, value,pos,weight):
        self.key = key
        self.value = value
        self.pos = pos
        self.weight = weight

def get_value_of_char_at_root(char):
    if char in vp_dict.root.children:
        return vp_dict.root.children[char].value
    return str(char)

def to_half_width(char):
    return full_width_punctuation.get(char, char)

def is_punctuation(token_key):
    return any(char in ".■?;：<[「!“\"\'" for char in token_key)


def is_special_token(token):
    # Check if token is ascii or fullwidth, halfwidth form unicode
    return all(ord(c) < 128 or 0xFF00 <= ord(c) <= 0xFFEF for c in token)


def is_ascii_alnum(s):
    return all(c.isalnum() and c.isascii() for c in s)

def process_tokenization(tokens):
    if not tokens:
        return ""
    
    add_cap = False
    add_bgap = False
    add_fgap = False
    pre_token = tokens[0]
    processed_tokens = []

    if tokens[0].value:
        tokens[0].value = capitalize_first(tokens[0].value)

    for token in tokens:
        token_value = token.value
        if len(token.key) == 1 and token.key in text_process.MtAttr.known_chars:
            token_value = to_half_width(token.key)
            char_attr = text_process.MtAttr.known_chars[token.key]
            add_cap = char_attr & text_process.MtAttr.Capn 
            add_bgap = not(char_attr & text_process.MtAttr.Undb)
            add_fgap = not(char_attr & text_process.MtAttr.Undn)
            if add_fgap:
                token_value = token_value + " "
                add_fgap = False
            if add_bgap:
                token_value = " " + token_value
                add_bgap = False
            processed_tokens.append(token_value)
        elif is_ascii_alnum(token.key):
            if not is_ascii_alnum(pre_token.key):
                token_value = " " + token_value
            processed_tokens.append(token_value)
        else:
            if add_cap:
                token_value = capitalize_first(token_value)
                add_cap = False
            if not pre_token.key in text_process.MtAttr.known_chars:
                token_value = " "+token_value 
            processed_tokens.append(token_value)
        pre_token = token
    return "".join(processed_tokens).strip()

def capitalize_first(s):
    return s[0].upper() + s[1:] if s else ""
            
def capitalize_first(s):
    if not s:
        return ""
    s = s.strip()
    return s[0].upper() + s[1:]

def load_dictionary_to_trie():
    vp_dict.load_dictionary_to_trie("VietPhrase.txt")
    name_dict.load_dictionary_to_trie("Names.txt")

def load_dictionary_to_map():
    with open("HV.txt", 'r', encoding="utf-8-sig") as file: 
        for text in file:
            key, _, value = text.strip().partition("=")  
            hv_map[key] = value.strip()

def init_dictionary():
    load_dictionary_to_trie()
    load_dictionary_to_map()
  

def process_token(root, pos, weight_factor, runes):
    char_index = 0 
    tokens = [] 

    current_char = runes[pos]
    if current_char not in root.children:
        # char = to_half_width(current_char)

        char = current_char
        tokens.append(Token(
            key=char,
            value=get_value_of_char_at_root(char),
            pos=pos,
            weight=weight_factor,
        ))
        return tokens

    while pos + char_index < len(runes) and runes[pos + char_index] in root.children:
        root = root.children[runes[pos + char_index]]
        if root and root.value:
            tokens.append(Token(
                key=''.join(runes[pos:pos + char_index + 1]),
                value=root.value,
                pos=pos,
                weight=weight_factor + char_index,
            ))
        char_index += 1

    return tokens
    
def process(runes, lang):
    result = ""
    match lang:
        case "hv":
            tokens = []
            for c in runes:
                tokens.append(Token(
                    key=c,
                    # value=to_half_width(hv_map.get(c, c)),
                    value=hv_map.get(c, c),
                    pos=0,
                    weight=0
                ))
            result = process_tokenization(tokens)
        case "vi":
            result = tokenize(runes)
        case _ :
            result = tokenize(runes)
    return result



def tokenize(text):
    runes = list(text)
    length = len(runes)

    best_choices = [None] * length
    best_weights = [-1] * (length + 1)
    best_weights[length] = 0

    choices = [[] for _ in range(length)]
   
    for i in range(length - 1, -1, -1):
        tokens_from_name = process_token(name_dict.root, i, 5, runes)
        tokens_from_vietphrase = process_token(vp_dict.root, i, 2, runes)
        choices[i].extend(tokens_from_name)
        choices[i].extend(tokens_from_vietphrase)
        for token in choices[i]:
            token_weight = token.weight
            next_index = i + len(token.key)
            if next_index <= length and (token_weight + best_weights[next_index]) > best_weights[i]:
                best_weights[i] = token_weight + best_weights[next_index]
                best_choices[i] = token

        if best_weights[i] == -1:
            best_weights[i] = 1
            best_choices[i] = Token(
                key=runes[i],
                # value=to_half_width(runes[i]),
                value=runes[i],
                pos=i,
                weight=1
            )

    result = []
    if length != 0:
        best_choices[0].value = capitalize_first(best_choices[0].value)
    while i < length:
        token = best_choices[i]
        result.append(token)
        i += len(token.key)
    
    return process_tokenization(result)

def translate(text,lang):
    match lang:
        case "hv":
            return process(text, "hv").strip()
        case "vi":
            return process(text, "vi").strip()
        case _ :
            return process(text)



