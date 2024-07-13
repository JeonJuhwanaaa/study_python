# << ISSUE >>

# We've got some buggy code, try running the code. The code will crash and give you a KeyError.
# This is because some of the posts in the facebook_posts don't have any "Likes".

# << OBJECTIVE >>

# Use what you've learnt about exception handling to prevent the program from crashing.

# --------------------------------------------------------------------------------------------

# eval() function will create a list of dictionaries using the input
facebook_posts = eval(input())

total_likes = 0
# TODO: Catch the KeyError exception

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass
    # 좋아요가 없는 항목은 건너뛰고 다음으로 넘어가서 좋아요만 있는 값만 더한다.

print(total_likes)


# input ->
# [{'Likes': 21, 'Comments': 2}, {'Likes': 13, 'Comments': 2, 'Shares': 1}, {'Likes': 33, 'Comments': 8, 'Shares': 3}, {'Comments': 4, 'Shares': 2},{'Comments': 1, 'Shares': 1}, {'Likes': 19, 'Comments': 3}]
