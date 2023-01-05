import easygui

path = easygui.fileopenbox("Select a file","Choose an article file","*.txt","*.txt",True)

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# Setup dictionary
harm = ['virtue', 'vice', 'all']
harm[0] = ["safe", "peace", "compassion", "empath", "sympath", "care", "caring", "protect", "shield", "shelter", "amity", "secur", "benefit", "defen", "guard", "preserve"]
harm[1] = ["harm", "suffer", "war", "wars", "warl", "warring", "fight", "violen", "hurt", "kill", "kills", "killer", "killed", "killing", "endanger", "cruel", "brutal", "abuse", "damag", "ruin", "ravage", "detriment", "crush", "attack", "annihilate", "destroy", "stomp", "abandon", "spurn", "impair", "exploit", "exploits", "exploited", "exploiting", "wound"]
harm[2] = harm[0] + harm[1]

fairness = ['virtue', 'vice', 'all']
fairness[0] = ["fair", "fairly", "fairness", "fair-", "fairmind", "fairplay", "equal", "justice", "justness", "justifi", "reciproc", "impartial", "egalitar", "rights", "equity", "evenness", "equivalent", "unbias", "tolerant", "equable", "balance", "homologous", "unprejudice", "reasonable", "constant", "honest"]
fairness[1] = ["unfair", "unequal", "bias", "unjust", "injust", "bigot", "discriminat", "disproportion", "inequitable", "prejud", "dishonest", "unscrupulous", "dissociate", "preference", "favoritism", "segregat", "exclusion", "exclud"]
fairness[2] = fairness[0] + fairness[1]

ingroup = ['virtue', 'vice', 'all']
ingroup[0] = ["together", "nation", "homeland", "family", "families", "familial", "group", "loyal", "patriot", "communal", "commune", "communit", "communis", "comrad", "cadre", "collectiv", "joint", "unison", "unite", "fellow", "guild", "solidarity", "devot", "member", "cliqu", "cohort", "ally", "insider", "segregat"]
ingroup[1] = ["abandon", "foreign", "enem", "betray", "treason", "traitor", "treacher", "disloyal", "individual", "apostasy", "apostate", "deserted", "deserter", "deserting", "deceiv", "jilt", "imposter", "miscreant", "spy", "sequester", "renegade", "terroris", "immigra"]
ingroup[2] = ingroup[0] + ingroup[1]

authority = ['virtue', 'vice', 'all']
authority[0] = ["preserve", "loyal", "obey", "obedien", "duty", "law", "lawful", "legal", "duti", "honor", "respect", "respectful", "respected", "respects", "order", "father", "mother", "motherl", "mothering", "mothers", "tradition", "hierarch", "authorit", "permit", "permission", "status", "rank", "leader", "class", "bourgeoisie", "caste", "position", "complian", "command", "supremacy", "control", "submi", "allegian", "serve", "abide", "defere", "defer", "revere", "venerat", "comply"]
authority[1] = ["betray", "treason", "traitor", "treacher", "disloyal", "apostasy", "apostate", "deserted", "deserter", "deserting", "defian", "rebel", "dissent", "subver", "disrespect", "disobe", "sediti", "agitat", "insubordinat", "illegal", "lawless", "insurgent", "mutinous", "defy", "dissident", "unfaithful", "alienate", "defector", "heretic", "nonconformist", "oppose", "protest", "refuse", "denounce", "remonstrate", "riot", "obstruct"]
authority[2] = authority[0] + authority[1]

purity = ['virtue', 'vice', 'all']
purity[0] = ["preserve", "piety", "pious", "purity", "pure", "clean", "steril", "sacred", "chast", "holy", "holiness", "saint", "wholesome", "celiba", "abstention", "virgin", "virgins", "virginity", "virginal", "austerity", "integrity", "modesty", "abstinen", "abstemiousness", "upright", "limpid", "unadulterated", "maiden", "virtuous", "refined", "decen", "immaculate", "innocent", "pristine", "church"]
purity[1] = ["ruin", "exploit", "exploits", "exploited", "exploiting", "apostasy", "apostate", "heretic", "disgust", "deprav", "disease", "unclean", "contagio", "indecen", "sin", "sinful", "sinner", "sins", "sinned", "sinning", "slut", "whore", "dirt", "impiety", "impious", "profan", "gross", "repuls", "sick", "promiscu", "lewd", "adulter", "debauche ", "defile", "tramp", "prostitut", "unchaste", "intemperate", "wanton", "profligate", "filth ", "trashy", "obscen", "lax", "taint", "stain", "tarnish", "debase", "desecrat", "wicked", "blemish", "exploitat", "pervert", "wretched"]
purity[2] = purity[0] + purity[1]

moralityGeneral = ["honest", "lawful", "legal", "piety", "pious", "wholesome", "integrity", "upright", "decen", "indecen", "wicked", "wretched", "righteous", "moral", "ethic", "value", "upstanding", "good", "goodness", "principle", "blameless", "exemplary", "lesson", "canon", "doctrine", "noble", "worth", "ideal", "praiseworthy", "commendable", "character", "proper", "laudable", "correct", "wrong", "evil", "immoral", "bad", "offend", "offensive", "transgress"]

# Create an empty dictionary
d = dict()

for article in path:
    # Open article
    text = open(article, "r")
  
    # Loop through each line of the file
    for line in text:
        # Remove the leading spaces and newline character
        line = line.strip()
    
        # Convert the characters in line to lowercase to avoid case mismatch
        line = line.lower()

        # Remove special characters
        line = line.replace(',','')
        line = line.replace('“','')
        line = line.replace('”','')
        line = line.replace('/','')
    
        # Split the line into words
        words = line.split(" ")
    
        # Iterate over each word in line
        for word in words:
            # Check if the word is already in dictionary
            if word in d:
                # Increment count of word by 1
                d[word] += 1
            else:
                # Add the word to dictionary with count 1
                d[word] = 1
  
sorted_dict = dict(sorted(d.items(), key=lambda item: item[1]))

# Harm
print(color.BOLD + color.GREEN + 'harmVirtue' + color.END + color.END)
harmVirtueCount = 0
for key in sorted(d, key=d.get, reverse=True):
    if key in harm[0]:
        harmVirtueCount += d[key]
        print(key, ":", d[key])
print()
print('total harmVirtue:',harmVirtueCount)
print()
print()

print(color.BOLD + color.RED + 'harmVice' + color.END + color.END)
harmViceCount = 0
for key in sorted(d, key=d.get, reverse=True):
    if key in harm[1]:
        harmViceCount += d[key]
        print(key, ":", d[key])
print()
print('total harmVice:',harmViceCount)
print()
print()

print(color.BOLD + color.PURPLE + 'harm' + color.END + color.END)
harmCount = 0
for key in sorted(d, key=d.get, reverse=True):
    if key in harm[2]:
        harmCount += d[key]
        print(key, ":", d[key])
print()
print('total harm:',harmCount)
print()
print()

# fairness
print(color.BOLD + color.GREEN + 'fairnessVirtue' + color.END + color.END)
fairnessVirtueCount = 0
for key in sorted(d, key=d.get, reverse=True):
    if key in fairness[0]:
        fairnessVirtueCount += d[key]
        print(key, ":", d[key])
print()
print('total fairnessVirtue:',fairnessVirtueCount)
print()
print()

print(color.BOLD + color.RED + 'fairnessVice' + color.END + color.END)
fairnessViceCount = 0
for key in sorted(d, key=d.get, reverse=True):
    if key in fairness[1]:
        fairnessViceCount += d[key]
        print(key, ":", d[key])
print()
print('total fairnessVice:',fairnessViceCount)
print()
print()

print(color.BOLD + color.PURPLE + 'fairness' + color.END + color.END)
fairnessCount = 0
for key in sorted(d, key=d.get, reverse=True):
    if key in fairness[2]:
        fairnessCount += d[key]
        print(key, ":", d[key])
print()
print('total fairness:',fairnessCount)
print()
print()

# ingroup
print(color.BOLD + color.GREEN + 'ingroupVirtue' + color.END + color.END)
ingroupVirtueCount = 0
for key in sorted(d, key=d.get, reverse=True):
    if key in ingroup[0]:
        ingroupVirtueCount += d[key]
        print(key, ":", d[key])
print()
print('total ingroupVirtue:',ingroupVirtueCount)
print()
print()

print(color.BOLD + color.RED + 'ingroupVice' + color.END + color.END)
ingroupViceCount = 0
for key in sorted(d, key=d.get, reverse=True):
    if key in ingroup[1]:
        ingroupViceCount += d[key]
        print(key, ":", d[key])
print()
print('total ingroupVice:',ingroupViceCount)
print()
print()

print(color.BOLD + color.PURPLE + 'ingroup' + color.END + color.END)
ingroupCount = 0
for key in sorted(d, key=d.get, reverse=True):
    if key in ingroup[2]:
        ingroupCount += d[key]
        print(key, ":", d[key])
print()
print('total ingroup:',ingroupCount)
print()
print()

# authority
print(color.BOLD + color.GREEN + 'authorityVirtue' + color.END + color.END)
authorityVirtueCount = 0
for key in sorted(d, key=d.get, reverse=True):
    if key in authority[0]:
        authorityVirtueCount += d[key]
        print(key, ":", d[key])
print()
print('total authorityVirtue:',authorityVirtueCount)
print()
print()

print(color.BOLD + color.RED + 'authorityVice' + color.END + color.END)
authorityViceCount = 0
for key in sorted(d, key=d.get, reverse=True):
    if key in authority[1]:
        authorityViceCount += d[key]
        print(key, ":", d[key])
print()
print('total authorityVice:',authorityViceCount)
print()
print()

print(color.BOLD + color.PURPLE + 'authority' + color.END + color.END)
authorityCount = 0
for key in sorted(d, key=d.get, reverse=True):
    if key in authority[2]:
        authorityCount += d[key]
        print(key, ":", d[key])
print()
print('total authority:',authorityCount)
print()
print()

# purity
print(color.BOLD + color.GREEN + 'purityVirtue' + color.END + color.END)
purityVirtueCount = 0
for key in sorted(d, key=d.get, reverse=True):
    if key in purity[0]:
        purityVirtueCount += d[key]
        print(key, ":", d[key])
print()
print('total purityVirtue:',purityVirtueCount)
print()
print()

print(color.BOLD + color.RED + 'purityVice' + color.END + color.END)
purityViceCount = 0
for key in sorted(d, key=d.get, reverse=True):
    if key in purity[1]:
        purityViceCount += d[key]
        print(key, ":", d[key])
print()
print('total purityVice:',purityViceCount)
print()
print()

print(color.BOLD + color.PURPLE + 'purity' + color.END + color.END)
purityCount = 0
for key in sorted(d, key=d.get, reverse=True):
    if key in purity[2]:
        purityCount += d[key]
        print(key, ":", d[key])
print()
print('total purity:',purityCount)
print()
print()

# morality
print(color.BOLD + color.YELLOW + 'moralityGeneral' + color.END + color.END)
moralityCount = 0
for key in sorted(d, key=d.get, reverse=True):
    if key in moralityGeneral:
        moralityCount += d[key]
        print(key, ":", d[key])
print()
print('total moralityGeneral:',moralityCount)
print()
print()
