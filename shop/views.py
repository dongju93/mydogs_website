from django.shortcuts import render, get_object_or_404
from shop.models import *
from cart.forms import AddProductForm
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.db.models import Sum, Avg, Count, Subquery

from order.models import Order, OrderItem, OrderTransaction
from coupon.models import Coupon
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



@login_required
def product_in_category(request, category_slug=None):
    current_category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available_display=True)
    cart = Cart(request)

    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=current_category)

    return render(request, 'shop/list.html',
                  {'current_category': current_category, 'categories': categories, 'products': products, 'cart':cart})

@login_required
def product_detail(request, id, product_slug=None):
    product = get_object_or_404(Product, id=id, slug=product_slug)
    add_to_cart = AddProductForm(initial={'quantity': 1})
    cart = Cart(request)

    return render(request, 'shop/detail.html', {'product': product, 'add_to_cart':add_to_cart, 'cart':cart})


from django.db import connections
import MySQLdb

def myorders(request):

    conn = MySQLdb.connect(
        host='origin.choijgtx1f2g.ap-northeast-2.rds.amazonaws.com', user='dongju', password='zz458976',
        db='origin', charset='utf8')

    cursor = conn.cursor()
    cursor.execute("SELECT trans.created, trans.order_id, pro.name, idid.quantity, idid.price, cou.code, oor.discount, trans.amount, oor.paid, oor.shipping, oor.last_name, oor.first_name, oor.phone, oor.email, oor.city, oor.address, oor.postal_code \
                    FROM order_order as oor, order_orderitem as idid, shop_product as pro, coupon_coupon as cou, order_ordertransaction as trans \
                    WHERE oor.id = idid.order_id and idid.product_id = pro.id and oor.coupon_id = cou.id and trans.order_id = oor.id and oor.orderuser_id = %s order by trans.created desc", [request.user.id])
    rows = cursor.fetchall()

    paginator = Paginator(rows, 5)  # Show 20 contacts per page
    page = request.GET.get('page')
    try:
        row = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        row = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        row = paginator.page(paginator.num_pages)

    return render(request, 'shop/myorders.html', {'row': row})