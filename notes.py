# function based view
# class based view 
# log-in decorator cant be used on classes !! 
# login mixin that is class inherit?  that will ass login functionality to the view 
#only the author of the post can update it. using userpassestestMixin, also we have
# loginrequiredmixin 
# UserPassesTestMixin comes with test func


# to add a json file to the database?
# >>> import json
# from blog.mode import Post "model"
# with open('post.json) as f:
#   post_json = json.load(f)
# for post in posts_json:
#   post = Post(title = post['title'], ...)
#   post.save()