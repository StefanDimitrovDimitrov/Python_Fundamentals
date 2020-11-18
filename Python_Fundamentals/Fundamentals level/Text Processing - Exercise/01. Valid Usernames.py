def is_containce(text):

    if 3 <= len(text) <= 16:

        if text.__contains__("-") or text.__contains__("_") or text.isalnum():
            return text

        else:
            return None


valid_user = []
user_names = input().split(", ")

for user in user_names:

    if is_containce(user):
        valid_user.append(user)

for word in valid_user:

    print(f'{"".join(word)}')
