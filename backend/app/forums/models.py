from ..database import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)
    description = db.Column(db.String(255))

    posts = db.relationship('Post', backref='category', lazy='dynamic')

    @classmethod
    def create(cls, name, description):
        category = cls(name=name, description=description)
        db.session.add(category)
        db.session.commit()
        return category

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, category_id):
        return cls.query.filter_by(id=category_id).first()

    def update(self, name, description):
        if name:
            self.name = name
        if description:
            self.description = description
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    body = db.Column(db.Text)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    comments = db.relationship('Comment', backref='post', lazy='dynamic')

    @classmethod
    def create(cls, title, body, category_id, author_id):
        post = cls(title=title, body=body, category_id=category_id, author_id=author_id)
        db.session.add(post)
        db.session.commit()
        return post

    @classmethod
    def get_all_by_category_id(cls, category_id):
        return cls.query.filter_by(category_id=category_id).all()

    @classmethod
    def get_by_id(cls, post_id):
        return cls.query.filter_by(id=post_id).first()

    @classmethod
    def get_by_id_and_category_id(cls, post_id, category_id):
        return cls.query.filter_by(id=post_id, category_id=category_id).first()

    def update(self, title=None, body=None, category_id=None):
        if title is not None:
            self.title = title
        if body is not None:
            self.body = body
        if category_id is not None:
            self.category_id = category_id
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    @classmethod
    def create(cls, body, post_id, author_id):
        comment = cls(body=body, post_id=post_id, author_id=author_id)
        db.session.add(comment)
        db.session.commit()
        return comment

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_comment_by_post_id_and_comment_id(cls, post_id, comment_id):
        return cls.query.filter_by(post_id=post_id, id=comment_id).first()

    @classmethod
    def get_by_post_id(cls, post_id):
        return cls.query.filter_by(post_id=post_id).all()

    def update(self, body):
        if body:
            self.body = body
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class PostLike(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))


class CommentLike(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'))
