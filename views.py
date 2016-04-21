from flask import Blueprint, redirect, request, render_template, url_for
from  flask.views import MethodView
from .models import Post, Comment
from flask_mongoengine.wtf import model_form

posts = Blueprint('posts',__name__,template_folder='templates')

class ListView(MethodView):
    def get(self):
        posts = Post.objects.all()
        return render_template('posts/list.html', posts=posts)

class DetailView(MethodView):
    form = model_form(Comment, exclude=['created_at'])

    def get_context(self, slug):
        post = Post.objects.get_or_404(slug=slug)
        form = self.form(request.form)

        context = {
            "post": post,
            "form": form
        }
        return context


    def get(self, slug):
        context = self.get_context(slug)
        return render_template('posts/detail.html', **context)
        # post = Post.objects.get_or_404(slug=slug)
        # return render_template('posts/detail.html', post=post)
    def post(self, slug):
        context = self.get_context(slug)
        form = context.get('form')

        if form.validate():
            comment = Comment()
            form.populate_obj(comment)

            post = context.get('post')
            post.comments.append(comment)
            post.save()

            return redirect(url_for('posts.detail',slug=slug))
        return render_template('posts/detail.html', **context)



posts.add_url_rule('/',view_func=ListView.as_view('list'))
posts.add_url_rule('/<slug>/',view_func=DetailView.as_view('detail'))

# @app.route('/')  # 访问的网址
# def index():
#     return render_template('index.html',test='my first blog website. \r Welcome ~',title='Untitled page')  # 返回渲染的网页
#
#
# @app.route('/login.html', methods=['GET', 'POST'])
# def login():
#     newform = LoginForm(request.form)
#     if request.method == 'POST':
#         password = newform.password
#         print('the password is :' + password.data)
#         return redirect('/')
#     return render_template('login.html',title='Login')
#
#
# if __name__ == "__main__":
#     app.run(debug=True)
