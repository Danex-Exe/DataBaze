from databaze import DataBaze

db = DataBaze()
users_db = db.file("users")
users_db.create()

users = {
    "member_1": {
        'id': '57699325',
        'messages': [
            'wow',
            'privet',
            'keep',
            'what',
            'wow',
            'wow',
            'wow',
            'do',
            'keep',
            'what',
            'clean'
        ],
        'status': 'online'
    },
    "member_2": {
        'id': '50394845',
        'messages': [
            'clean',
            'privet',
            'up',
            'privet',
            'sleep',
            'up',
            'wow',
            'what',
            'keep',
            'up',
            'sleep'
        ],
        'status': 'offline'
    },
    "member_3": {
        'id': '11130836',
        'messages': [
            'test',
            'keep'
        ],
        'status': 'online'
    },
    "member_4": {
        'id': '46617689',
        'messages': [
            'up',
            'clean',
            'privet',
            'up',
            'privet',
            'test',
            'clean',
            'sleep',
            'keep'
        ],
        'status': 'offline'
    },
    "member_5": {
        'id': '97656290',
        'messages': [
            'up',
            'do',
            'privet',
            'privet',
            'keep',
            'clean',
            'do',
            'keep',
            'privet',
            'sleep',
            'test',
            'sleep',
            'wow',
            'keep'
        ],
        'status': 'online'
    },
    "member_6": {
        'id': '80612061',
        'messages': [
            'test',
            'up',
            'what'
        ],
        'status': 'online'
    },
    "member_7": {
        'id': '47113209',
        'messages': [
            'up',
            'test',
            'do',
            'sleep',
            'sleep',
            'do'
        ],
        'status': 'online'
    },
    "member_8": {
        'id': '54000286',
        'messages': [
            'clean',
            'what'
        ],
        'status': 'online'
    },
    "member_9": {
        'id': '11910683',
        'messages': [
            'what',
            'do',
            'sleep',
            'keep',
            'wow',
            'privet',
            'sleep',
            'test',
            'keep',
            'clean',
            'wow',
            'sleep',
            'clean',
            'keep'
        ],
        'status': 'offline'
    },
    "member_10": {
        'id': '61113349',
        'messages': [
            'wow',
            'wow',
            'up',
            'keep',
            'keep',
            'up',
            'sleep',
            'keep',
            'up',
            'what',
            'test',
            'up',
            'keep',
            'wow'
        ],
        'status': 'online'
    },
    "member_11": {
        'id': '45825105',
        'messages': [
            'do',
            'privet',
            'wow',
            'test',
            'what',
            'up',
            'test',
            'test',
            'what',
            'sleep',
            'wow',
            'up',
            'up',
            'test'
        ],
        'status': 'online'
    },
    "member_12": {
        'id': '04329861',
        'messages': [
            'keep',
            'up',
            'what',
            'clean',
            'sleep',
            'wow',
            'do',
            'privet',
            'clean',
            'clean',
            'keep',
            'clean',
            'clean',
            'what',
            'test'
        ],
        'status': 'offline'
    },     
    "member_13": {
        'id': '76358801',
        'messages': [
            'test',
            'wow',
            'wow',
            'up',
            'up',
            'what',
            'clean',
            'sleep',
            'sleep'
        ],
        'status': 'offline'
    },
    "member_14": {
        'id': '35072237',
        'messages': [
            'what',
            'sleep'
        ],
        'status': 'online'
    },
    "member_15": {
        'id': '47212230',
        'messages': [
            'do',
            'clean',
            'keep',
            'do',
            'clean',
            'do',
            'keep',
            'clean',
            'clean',
            'privet',
            'clean',
            'privet',
            'privet'
        ],
        'status': 'offline'
    },
    "member_16": {
        'id': '85280862',
        'messages': [
            'keep',
            'sleep',
            'test',
            'wow',
            'what',
            'do',
            'clean',
            'up',
            'clean'
        ],
        'status': 'offline'
    },
    "member_17": {
        'id': '92635339',
        'messages': [
            'up',
            'do',
            'wow'
        ],
        'status': 'offline'
    },
    "member_18": {
        'id': '93099502',
        'messages': [
            'keep',
            'up',
            'what',
            'test'
        ],
        'status': 'offline'
    },
    "member_19": {
        'id': '87086048',
        'messages': [
            'do',
            'wow',
            'keep',
            'keep',
            'test',
            'do',
            'up',
            'wow',
            'sleep',
            'do',
            'sleep'
        ],
        'status': 'offline'
    },
    "member_20": {
        'id': '85365171',
        'messages': [
            'what',
            'clean',
            'keep',
            'do',
            'do',
            'keep',
            'test',
            'wow',
            'wow',
            'test',
            'wow'
        ],
        'status': 'online'
    },
    "member_21": {
        'id': '17187212',
        'messages': [
            'clean',
            'sleep',
            'privet'
        ],
        'status': 'online'
    },
    "member_22": {
        'id': '88714506',
        'messages': [
            'clean',
            'privet',
            'wow',
            'what',
            'up',
            'what',
            'keep',
            'up',
            'what',
            'privet',
            'privet'
        ],
        'status': 'online'
    },
    "member_23": {
        'id': '95601800',
        'messages': [
            'wow',
            'wow',
            'what',
            'up',
            'test',
            'test'
        ],
        'status': 'online'
    },
    "member_24": {
        'id': '01003051',
        'messages': [
            'do',
            'what',
            'sleep',
            'test',
            'up',
            'what',
            'keep',
            'privet',
            'keep',
            'privet',
            'privet',
            'what',
            'test'
        ],
        'status': 'online'
    },
    "member_25": {
        'id': '24692662',
        'messages': [
            'do',
            'test',
            'do',
            'keep',
            'privet',
            'privet',
            'privet',
            'test',
            'sleep',
            'keep'
        ],
        'status': 'offline'
    },
    "member_26": {
        'id': '69345898',
        'messages': [
            'wow',
            'sleep',
            'wow',
            'do'
        ],
        'status': 'offline'
    },
    "member_27": {
        'id': '38953938',
        'messages': [
            'sleep',
            'privet',
            'privet',
            'wow',
            'up',
            'sleep',
            'wow',
            'clean',
            'what',
            'privet',
            'do',
            'do',
            'keep',
            'privet'
        ],
        'status': 'online'
    },
    "member_28": {
        'id': '89054244',
        'messages': [
            'privet',
            'privet',
            'keep',
            'do',
            'up',
            'do',
            'test',
            'keep'
        ],
        'status': 'online'
    },
    "member_29": {
        'id': '33626861',
        'messages': [
            'privet',
            'do',
            'clean',
            'clean',
            'sleep',
            'clean',
            'up',
            'clean',
            'up'
        ],
        'status': 'offline'
    },
    "member_30": {
        'id': '59891729',
        'messages': [
            'test',
            'wow',
            'up',
            'test',
            'test',
            'sleep',
            'keep',
            'keep',
            'sleep',
            'do',
            'do',
            'test'
        ],
        'status': 'online'
    },
    "member_31": {
        'id': '83324960',
        'messages': [
            'test',
            'wow',
            'keep',
            'what',
            'clean',
            'wow',
            'keep',
            'up',
            'clean',
            'sleep',
            'sleep',
            'wow'
        ],
        'status': 'online'
    },
    "member_32": {
        'id': '29968124',
        'messages': [
            'what',
            'privet',
            'test',
            'wow',
            'do',
            'do'
        ],
        'status': 'offline'
    },
    "member_33": {
        'id': '24952867',
        'messages': [
            'test',
            'wow',
            'what',
            'up',
            'do',
            'privet',
            'keep',
            'keep',
            'what',
            'do',
            'wow',
            'wow',
            'up',
            'privet'
        ],
        'status': 'online'
    },
    "member_34": {
        'id': '19736789',
        'messages': [
            'clean',
            'wow',
            'up',
            'sleep',
            'up',
            'what',
            'what',
            'what',
            'test',
            'test',
            'keep',
            'do',
            'clean'
        ],
        'status': 'online'
    },
    "member_35": {
        'id': '67405670',
        'messages': [
            'do',
            'clean',
            'test',
            'test',
            'sleep'
        ],
        'status': 'online'
    },
    "member_36": {
        'id': '90792905',
        'messages': [
            'clean',
            'what',
            'clean',
            'what',
            'clean',
            'privet'
        ],
        'status': 'offline'
    },
    "member_37": {
        'id': '24167865',
        'messages': [
            'up',
            'sleep',
            'test',
            'sleep',
            'privet',
            'privet',
            'up',
            'do',
            'clean',
            'what',
            'privet',
            'what'
        ],
        'status': 'online'
    },
    "member_38": {
        'id': '92081098',
        'messages': [
            'test',
            'wow',
            'wow',
            'clean',
            'privet'
        ],
        'status': 'online'
    },
    "member_39": {
        'id': '63618836',
        'messages': [
            'sleep',
            'test',
            'privet',
            'keep',
            'test'
        ],
        'status': 'offline'
    },
    "member_40": {
        'id': '35490808',
        'messages': [
            'what',
            'keep',
            'privet',
            'what',
            'sleep',
            'keep',
            'wow',
            'test',
            'privet',
            'sleep',
            'keep'
        ],
        'status': 'offline'
    },
    "member_41": {
        'id': '03843078',
        'messages': [
            'do',
            'clean',
            'sleep'
        ],
        'status': 'online'
    },
    "member_42": {
        'id': '38889339',
        'messages': [
            'clean',
            'do',
            'privet',
            'clean',
            'up',
            'do',
            'privet',
            'test',
            'do'
        ],
        'status': 'online'
    },
    "member_43": {
        'id': '16360833',
        'messages': [
            'test',
            'clean',
            'test',
            'do',
            'what',
            'sleep',
            'keep',
            'sleep',
            'wow'
        ],
        'status': 'offline'
    },
    "member_44": {
        'id': '59986883',
        'messages': [
            'privet',
            'clean',
            'do',
            'clean',
            'up',
            'wow',
            'wow',
            'clean',
            'test'
        ],
        'status': 'offline'
    },
    "member_45": {
        'id': '85907358',
        'messages': [
            'keep',
            'clean',
            'test',
            'up',
            'wow',
            'test',
            'sleep'
        ],
        'status': 'offline'
    },
    "member_46": {
        'id': '43687154',
        'messages': [
            'privet',
            'do',
            'do',
            'do',
            'test',
            'test',
            'what',
            'do',
            'do',
            'sleep',
            'wow',
            'do'
        ],
        'status': 'offline'
    },
    "member_47": {
        'id': '92368229',
        'messages': [
            'do',
            'wow',
            'sleep',
            'up',
            'privet',
            'sleep',
            'wow',
            'do',
            'what',
            'keep',
            'what',
            'privet',
            'what',
            'sleep'
        ],
        'status': 'online'
    },
    "member_48": {
        'id': '49660810',
        'messages': [
            'keep',
            'what',
            'up',
            'clean',
            'keep'
        ],
        'status': 'online'
    },
    "member_49": {
        'id': '83509543',
        'messages': [
            'wow',
            'what',
            'wow',
            'do',
            'wow',
            'test',
            'privet',
            'do',
            'what',
            'clean',
            'clean'
        ],
        'status': 'online'
    },
    "member_50": {
        'id': '01406782',
        'messages': [
            'up',
            'test',
            'keep',
            'keep',
            'wow',
            'what',
            'up',
            'do',
            'up'
        ],
        'status': 'online'
    },
    "member_51": {
        'id': '46844810',
        'messages': [
            'sleep',
            'what'
        ],
        'status': 'online'
    },
    "member_52": {
        'id': '87549491',
        'messages': [
            'test',
            'wow',
            'what',
            'privet',
            'do',
            'what',
            'clean',
            'what',
            'keep',
            'keep',
            'sleep',
            'clean',
            'test',
            'clean'
        ],
        'status': 'online'
    },
    "member_53": {
        'id': '12290183',
        'messages': [
            'sleep',
            'do',
            'do',
            'keep',
            'wow',
            'up',
            'sleep',
            'up',
            'keep',
            'do',
            'up',
            'up',
            'test',
            'privet',
            'what'
        ],
        'status': 'offline'
    },
    "member_54": {
        'id': '76498428',
        'messages': [
            'keep'
        ],
        'status': 'offline'
    },
    "member_55": {
        'id': '45349418',
        'messages': [
            'test',
            'wow',
            'up',
            'sleep',
            'what'
        ],
        'status': 'online'
    },
    "member_56": {
        'id': '03807895',
        'messages': [
            'keep',
            'up'
        ],
        'status': 'offline'
    },
    "member_57": {
        'id': '88348641',
        'messages': [
            'clean',
            'wow'
        ],
        'status': 'online'
    },
    "member_58": {
        'id': '29534055',
        'messages': [
            'keep',
            'up'
        ],
        'status': 'online'
    },
    "member_59": {
        'id': '20903380',
        'messages': [
            'sleep',
            'clean',
            'test',
            'sleep'
        ],
        'status': 'offline'
    },
    "member_60": {
        'id': '11091316',
        'messages': [
            'sleep',
            'test',
            'privet',
            'what',
            'do',
            'wow'
        ],
        'status': 'online'
    },
    "member_61": {
        'id': '49270598',
        'messages': [
            'privet',
            'keep',
            'up',
            'keep',
            'wow',
            'up',
            'clean',
            'keep',
            'privet',
            'sleep',
            'clean',
            'wow',
            'test',
            'clean'
        ],
        'status': 'online'
    },
    "member_62": {
        'id': '83054633',
        'messages': [
            'clean',
            'sleep'
        ],
        'status': 'online'
    },
    "member_63": {
        'id': '09703364',
        'messages': [
            'what',
            'privet',
            'what',
            'what',
            'do',
            'privet',
            'up'
        ],
        'status': 'offline'
    },
    "member_64": {
        'id': '40530431',
        'messages': [
            'sleep',
            'privet',
            'test',
            'keep',
            'clean',
            'clean',
            'wow',
            'keep'
        ],
        'status': 'online'
    },
    "member_65": {
        'id': '36513307',
        'messages': [
            'clean',
            'up'
        ],
        'status': 'online'
    },
    "member_66": {
        'id': '64284162',
        'messages': [
            'sleep',
            'sleep',
            'privet',
            'keep',
            'do',
            'privet',
            'keep',
            'privet'
        ],
        'status': 'offline'
    },
    "member_67": {
        'id': '26130473',
        'messages': [
            'wow',
            'clean',
            'keep',
            'sleep',
            'privet',
            'privet'
        ],
        'status': 'online'
    },
    "member_68": {
        'id': '74594332',
        'messages': [
            'sleep',
            'wow',
            'test',
            'what',
            'test',
            'privet',
            'what'
        ],
        'status': 'online'
    },
    "member_69": {
        'id': '86414186',
        'messages': [
            'clean',
            'test'
        ],
        'status': 'online'
    },
    "member_70": {
        'id': '45993797',
        'messages': [
            'up',
            'up',
            'keep',
            'privet',
            'do'
        ],
        'status': 'online'
    },
    "member_71": {
        'id': '14204494',
        'messages': [
            'keep'
        ],
        'status': 'offline'
    },
    "member_72": {
        'id': '31617724',
        'messages': [
            'test',
            'sleep',
            'do',
            'clean',
            'test',
            'wow',
            'keep',
            'wow',
            'privet',
            'do',
            'what',
            'keep',
            'up',
            'keep',
            'what'
        ],
        'status': 'offline'
    },
    "member_73": {
        'id': '58137030',
        'messages': [
            'clean',
            'sleep',
            'do',
            'do',
            'privet',
            'wow',
            'do',
            'what',
            'sleep'
        ],
        'status': 'online'
    },
    "member_74": {
        'id': '96631243',
        'messages': [
            'wow',
            'what',
            'sleep',
            'keep',
            'clean',
            'up',
            'privet',
            'up',
            'privet',
            'wow',
            'up',
            'do'
        ],
        'status': 'online'
    },
    "member_75": {
        'id': '12079957',
        'messages': [
            'test',
            'test',
            'keep',
            'wow',
            'up',
            'do'
        ],
        'status': 'online'
    },
    "member_76": {
        'id': '91790159',
        'messages': [
            'wow',
            'sleep',
            'sleep',
            'do'
        ],
        'status': 'offline'
    },
    "member_77": {
        'id': '27547179',
        'messages': [
            'privet',
            'clean'
        ],
        'status': 'online'
    },
    "member_78": {
        'id': '53558885',
        'messages': [
            'sleep',
            'up',
            'up',
            'sleep',
            'what',
            'clean',
            'privet',
            'privet',
            'up',
            'wow',
            'keep'
        ],
        'status': 'offline'
    },
    "member_79": {
        'id': '93217489',
        'messages': [
            'test',
            'keep',
            'test',
            'clean',
            'privet',
            'privet',
            'test',
            'do',
            'what',
            'keep',
            'do',
            'keep',
            'what'
        ],
        'status': 'online'
    },
    "member_80": {
        'id': '54749173',
        'messages': [
            'sleep',
            'clean',
            'test',
            'wow',
            'wow',
            'wow',
            'keep',
            'test',
            'do',
            'test',
            'test',
            'sleep',
            'keep',
            'what',
            'up'
        ],
        'status': 'online'
    },
    "member_81": {
        'id': '67661174',
        'messages': [
            'what',
            'sleep',
            'keep'
        ],
        'status': 'online'
    },
    "member_82": {
        'id': '15631787',
        'messages': [
            'do',
            'privet',
            'sleep',
            'do',
            'wow',
            'keep',
            'what'
        ],
        'status': 'offline'
    },
    "member_83": {
        'id': '64609970',
        'messages': [
            'privet',
            'what'
        ],
        'status': 'online'
    },
    "member_84": {
        'id': '99121602',
        'messages': [
            'up',
            'up',
            'privet',
            'what',
            'do',
            'clean',
            'keep',
            'do',
            'keep',
            'wow',
            'wow',
            'do',
            'sleep',
            'test'
        ],
        'status': 'offline'
    },
    "member_85": {
        'id': '08085703',
        'messages': [
            'sleep',
            'what',
            'what',
            'test',
            'sleep',
            'privet',
            'what'
        ],
        'status': 'online'
    },
    "member_86": {
        'id': '20183485',
        'messages': [
            'clean',
            'do',
            'sleep',
            'test',
            'wow',
            'wow',
            'do'
        ],
        'status': 'offline'
    },
    "member_87": {
        'id': '08053204',
        'messages': [
            'test',
            'what',
            'what',
            'do',
            'wow',
            'clean',
            'keep',
            'test',
            'keep',
            'test',
            'keep'
        ],
        'status': 'online'
    },
    "member_88": {
        'id': '36649440',
        'messages': [
            'wow',
            'do'
        ],
        'status': 'offline'
    },
    "member_89": {
        'id': '23097521',
        'messages': [
            'privet',
            'keep',
            'keep'
        ],
        'status': 'online'
    },
    "member_90": {
        'id': '68972771',
        'messages': [
            'what',
            'what',
            'up',
            'wow',
            'wow'
        ],
        'status': 'online'
    },
    "member_91": {
        'id': '78676668',
        'messages': [
            'what',
            'privet',
            'sleep',
            'keep',
            'what',
            'keep',
            'keep',
            'test',
            'wow',
            'do',
            'privet',
            'keep',
            'test',
            'up',
            'test'
        ],
        'status': 'offline'
    },        
    "member_92": {
        'id': '17640128',
        'messages': [
            'up',
            'keep',
            'test',
            'clean',
            'sleep',
            'privet',
            'wow',
            'wow',
            'do',
            'up',
            'what'
        ],
        'status': 'online'
    },
    "member_93": {
        'id': '13484033',
        'messages': [
            'what',
            'test',
            'privet',
            'clean',
            'test',
            'keep',
            'do',
            'do',
            'keep',
            'do',
            'up',
            'keep',
            'test',
            'do',
            'up'
        ],
        'status': 'online'
    },
    "member_94": {
        'id': '76329367',
        'messages': [
            'privet',
            'clean',
            'up',
            'what',
            'do',
            'keep',
            'do',
            'what'
        ],
        'status': 'online'
    },
    "member_95": {
        'id': '19892919',
        'messages': [
            'do',
            'sleep',
            'privet',
            'keep',
            'clean',
            'test',
            'keep',
            'keep',
            'keep',
            'what',
            'privet',
            'what'
        ],
        'status': 'online'
    },
    "member_96": {
        'id': '60932754',
        'messages': [
            'do',
            'do',
            'keep',
            'sleep',
            'up'
        ],
        'status': 'offline'
    },
    "member_97": {
        'id': '53397013',
        'messages': [
            'what',
            'test',
            'clean',
            'clean',
            'test',
            'clean',
            'keep',
            'privet',
            'what',
            'what',
            'keep',
            'what',
            'privet',
            'what',
            'do'
        ],
        'status': 'online'
    },    
    "member_98": {
        'id': '96355087',
        'messages': [
            'clean',
            'wow',
            'sleep'
        ],
        'status': 'offline'
    },
    "member_99": {
        'id': '14623064',
        'messages': [
            'keep',
            'privet',
            'do',
            'privet',
            'wow',
            'sleep',
            'do',
            'sleep',
            'clean'
        ],
        'status': 'offline'
    },
    "member_100": {
        'id': '03964079',
        'messages': [
            'test',
            'privet',
            'keep',
            'clean',
            'up',
            'sleep',
            'sleep',
            'up',
            'test',
            'what',
            'test'
        ],
        'status': 'offline'
    }
}

users_db.write(users)