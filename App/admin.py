from App.models import Category, Product, UserRole
from App import app, db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose
from flask_login import logout_user, current_user
from flask import redirect

admin = Admin(app, name="Quản trị bán hàng", template_mode="bootstrap4")


class AuthenticateAdmin(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRole.ADMIN


class AuthenticateUser(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated


class MyProductView(AuthenticateAdmin):
    column_list = ["id", "name", "price", "active"]
    column_filters = ["name", "price"]
    column_searchable_list = ["name"]
    column_editable_list = ["name", "price"]
    edit_modal = True


class MyCategoryView(AuthenticateAdmin):
    column_list = ["id", "name", "products"]


class StatsView(AuthenticateUser):
    @expose("/")
    def index(self):
        return self.render("admin/stats.html")


class LogoutView(AuthenticateUser):
    @expose("/")
    def index(self):
        logout_user()
        return redirect("/admin")


admin.add_view(MyCategoryView(Category, db.session))
admin.add_view(MyProductView(Product, db.session))
admin.add_view(StatsView(name="Thống kê báo cáo"))
admin.add_view(LogoutView(name="Đăng xuất"))
