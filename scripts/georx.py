import re
GEO=re.compile(r"\bBasilicata\b|\bLucania\b|\bLucanian?\b|(?-i:\bPotenza\b)(?! Picena)|(?-i:\bMatera\b)|\bMelfi\b|\bPolicoro\b|\bPisticci\b|\bBernalda\b|Metapont(o|um|ino)|Val d.Agri|Agri [Vv]alley|\bViggiano\b|\bMaratea\b|\bLagonegro\b|Rionero|Monte Vulture|Mount Vulture|(?-i:\bVulture\b)(?= area| region| district)|\bPollino\b|\bBasento\b|\bBradano\b|\bSinni\b|(?-i:\bVenosa\b)|(?-i:\bIRCCS CROB\b|\bCROB\b)|San Carlo (Regional |General )?(Hospital|hospital)(?! Borromeo)|Ospedale San Carlo(?! Borromeo)|Azienda Ospedaliera Regionale San Carlo|Madonna delle Grazie",re.I)
WILD=re.compile(r"south(ern)?[- ]Italy|Ionian|Tyrrhenian",re.I)
AFF=re.compile(r"Basilicata|Potenza(?! Picena)|Matera|Lucania|Rionero|Melfi|Policoro|\bCROB\b",re.I)
