social = {'Insta': 'instaUsername', 'fb': 'fbusername', 'linkedin': 'linUsr', 'twitter': 'xursname'}
print(social)
for name in social:
    print("social-", name, ": ", social[name])
for key, value in social.items():
    print(key, value)
if 'reddit' in social:
    print("Yes, reddit is avilable in socials")