# fonts.py

# REAL FONT MAPS

BOLD = str.maketrans({
    'A':'𝗔','B':'𝗕','C':'𝗖','D':'𝗗','E':'𝗘','F':'𝗙','G':'𝗚','H':'𝗛','I':'𝗜','J':'𝗝',
    'K':'𝗞','L':'𝗟','M':'𝗠','N':'𝗡','O':'𝗢','P':'𝗣','Q':'𝗤','R':'𝗥','S':'𝗦','T':'𝗧',
    'U':'𝗨','V':'𝗩','W':'𝗪','X':'𝗫','Y':'𝗬','Z':'𝗭',
    'a':'𝗮','b':'𝗯','c':'𝗰','d':'𝗱','e':'𝗲','f':'𝗳','g':'𝗴','h':'𝗵','i':'𝗶','j':'𝗷',
    'k':'𝗸','l':'𝗹','m':'𝗺','n':'𝗻','o':'𝗼','p':'𝗽','q':'𝗾','r':'𝗿','s':'𝘀','t':'𝘁',
    'u':'𝘂','v':'𝘃','w':'𝘄','x':'𝘅','y':'𝘆','z':'𝘇'
})

ITALIC = str.maketrans({
    'A':'𝘈','B':'𝘉','C':'𝘊','D':'𝘋','E':'𝘌','F':'𝘍','G':'𝘎','H':'𝘏','I':'𝘐','J':'𝘑',
    'K':'𝘒','L':'𝘓','M':'𝘔','N':'𝘕','O':'𝘖','P':'𝘗','Q':'𝘘','R':'𝘙','S':'𝘚','T':'𝘛',
    'U':'𝘜','V':'𝘝','W':'𝘞','X':'𝘟','Y':'𝘠','Z':'𝘡'
})

BOLD_ITALIC = str.maketrans({
    'A':'𝘼','B':'𝘽','C':'𝘾','D':'𝘿','E':'𝙀','F':'𝙁','G':'𝙂','H':'𝙃','I':'𝙄','J':'𝙅',
    'K':'𝙆','L':'𝙇','M':'𝙈','N':'𝙉','O':'𝙊','P':'𝙋','Q':'𝙌','R':'𝙍','S':'𝙎','T':'𝙏',
    'U':'𝙐','V':'𝙑','W':'𝙒','X':'𝙓','Y':'𝙔','Z':'𝙕'
})

MONO = str.maketrans({
    'A':'𝙰','B':'𝙱','C':'𝙲','D':'𝙳','E':'𝙴','F':'𝙵','G':'𝙶','H':'𝙷','I':'𝙸','J':'𝙹',
    'K':'𝙺','L':'𝙻','M':'𝙼','N':'𝙽','O':'𝙾','P':'𝙿','Q':'𝚀','R':'𝚁','S':'𝚂','T':'𝚃',
    'U':'𝚄','V':'𝚅','W':'𝚆','X':'𝚇','Y':'𝚈','Z':'𝚉'
})

DOUBLE = str.maketrans({
    'A':'𝔸','B':'𝔹','C':'ℂ','D':'𝔻','E':'𝔼','F':'𝔽','G':'𝔾','H':'ℍ','I':'𝕀','J':'𝕁',
    'K':'𝕂','L':'𝕃','M':'𝕄','N':'ℕ','O':'𝕆','P':'ℙ','Q':'ℚ','R':'ℝ','S':'𝕊','T':'𝕋',
    'U':'𝕌','V':'𝕍','W':'𝕎','X':'𝕏','Y':'𝕐','Z':'ℤ'
})


# FUNCTIONS

def small_caps(text):
    table = {
        "a":"ᴀ","b":"ʙ","c":"ᴄ","d":"ᴅ","e":"ᴇ","f":"ꜰ","g":"ɢ","h":"ʜ",
        "i":"ɪ","j":"ᴊ","k":"ᴋ","l":"ʟ","m":"ᴍ","n":"ɴ","o":"ᴏ","p":"ᴘ",
        "q":"ǫ","r":"ʀ","s":"ꜱ","t":"ᴛ","u":"ᴜ","v":"ᴠ","w":"ᴡ","x":"x",
        "y":"ʏ","z":"ᴢ"
    }
    return ''.join(table.get(c, c) for c in text.lower())

def boxed(text):
    return f"【{text}】"

def fancy(text):
    return f"꧁{text}꧂"

def crown(text):
    return f"♛ {text} ♛"

def fire(text):
    return f"🔥 {text} 🔥"

def star(text):
    return f"★ {text} ★"

def diamond(text):
    return f"◆ {text} ◆"

def heart(text):
    return f"♥ {text} ♥"

def arrow(text):
    return f"➤ {text} ◄"

def king(text):
    return f"♔ {text} ♔"

def queen(text):
    return f"♕ {text} ♕"

def lightning(text):
    return f"⚡ {text} ⚡"

def skull(text):
    return f"☠ {text} ☠"

def flower(text):
    return f"🌹 {text} 🌹"

def rocket(text):
    return f"🚀 {text} 🚀"
