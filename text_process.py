
class MtAttr():
    # nominal characteristics
    # Ndes = 0x1
    # Ntmp = 0x2
    # Nper = 0x4
    # Nloc = 0x8
    # Norg = 0x16

    # # shared characteristics
    # At_h = 0x32
    # At_t = 0x64
    # Prfx = 0x128
    # Sufx = 0x256

    # # grammar/punctuation:
    # Hide = 0x512
    # Asis = 0x1024
    Capn = 0x0001
    Capx = 0x0010
    Undb = 0x0100
    Undn = 0x1000

    # # verbal characteristics
    # Vpst = 0x32768
    # Vmod = 0x65536
    # Vpsy = 0x131072
    # Vint = 0x262144
    # Vdit = 0x524288

    # # pronoun types (unused)
    # Pn_d = 0x1048576
    # Pn_i = 0x2097152


   

    known_chars = {
        ' ': Capn | Undb | Undn,
        '＀': Capn | Undb | Undn,
        '!': Capn | Undb | Undn,
        '　': Capn | Undb | Undn,
        '！': Capn | Undb,
        '＂': Capx | Undb | Undn,
        '＃': Capx | Undn,
        '＄': Capx | Undn,
        '％': Capx | Undb,
        '＆': Capx | Undb | Undn,
        '＇': Capx | Undb | Undn,
        '（':  Undn,
        '）': Capx | Undb,
        '＊': Capx | Undb | Undn,
        '＋': Capx | Undb | Undn,
        ',':  Undb,
        '，':  Undb,
        '－': Capx | Undb | Undn,
        '．': Capn | Undb,
        '／': Capx | Undb | Undn,
        '：': Capn | Undb,
        '；': Capx | Undb,
        '＜': Undn,
        '＝': Capx | Undb | Undn,
        '＞': Capn | Undb,
        '？': Capn | Undb,
        '＠': Capx | Undn,
        '［': Capx | Undn,
        '＼': Capx | Undb | Undn,
        '］': Capx | Undb,
        '＾': Capx | Undb | Undn,
        '＿': Capx | Undb | Undn,
        '｀': Capx | Undn,
        '｛': Capx | Undn,
        '｜': Capx | Undb | Undn,
        '｝': Capx | Undb,
        '～': Capx | Undb,
        '｟': Capx | Undn,
        '｠': Capx | Undb,
        '｡': Capn | Undb,
        '。': Capn | Undb,
        '｢': Capn | Undn,
        '｣': Capx | Undb,
        '､': Capx | Undb,
        '、': Capx | Undb,
        '･': Capx | Undb | Undn,
        '‧': Capx | Undb | Undn,
        '.': Capn | Undb,
        '·': Capx | Undb | Undn,
        '〈': Capn | Undn,
        '〉': Capx | Undb,
        '《':  Undn,
        '》': Capx | Undb,
        '‹': Undn,
        '›': Capx | Undb,
        '“': Capx | Undn,
        '‘': Capx | Undn,
        '”': Capx | Undb,
        '’': Capx | Undb,
        '…': Capx | Undb,
    }




