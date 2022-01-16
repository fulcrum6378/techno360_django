from django.db import models as m

NAME_LENGTH = 100
DESC_LENGTH = 1000


class Category(m.Model):
    slug = m.SlugField(primary_key=True, unique=True)
    name = m.CharField(max_length=NAME_LENGTH)
    desc = m.TextField(max_length=DESC_LENGTH, blank=True, null=True)
    cate = m.SlugField(blank=True, null=True)


class Contractual(m.Model):
    slug = m.SlugField(primary_key=True, unique=True)
    name = m.CharField(max_length=NAME_LENGTH)
    desc = m.TextField(max_length=DESC_LENGTH, blank=True, null=True)
    pric = m.PositiveIntegerField()
    cate = m.ForeignKey(Category, on_delete=m.SET_NULL, null=True)


class Product(m.Model):
    slug = m.SlugField(primary_key=True, unique=True)
    name = m.CharField(max_length=NAME_LENGTH)
    desc = m.TextField(max_length=DESC_LENGTH, blank=True, null=True)
    date = m.DateTimeField(auto_now_add=True)
    pric = m.PositiveSmallIntegerField(default=0)
    cate = m.ForeignKey(Category, on_delete=m.SET_NULL, null=True)


class User(m.Model):
    id = m.BigAutoField(primary_key=True)
    fnam = m.CharField(max_length=75)
    lnam = m.CharField(max_length=75)
    mail = m.CharField(max_length=125)
    phon = m.CharField(max_length=15, null=True, blank=True)
    join = m.DateTimeField(auto_now_add=True)
    actv = m.DateTimeField(auto_now=True)


class Purchase(m.Model):
    user = m.ForeignKey(User, on_delete=m.CASCADE)
    prod = m.ForeignKey(Product, on_delete=m.PROTECT)
    cret = m.DateTimeField(auto_now_add=True)
    paid = m.DateTimeField(null=True, blank=True)
    dliv = m.DateTimeField(null=True, blank=True)
    link = m.URLField(null=True, blank=True)


class Contract(m.Model):
    user = m.ForeignKey(User, on_delete=m.CASCADE)
    cont = m.ForeignKey(Contractual, on_delete=m.PROTECT)
    date = m.DateTimeField(auto_now_add=True)
    desc = m.TextField(max_length=3000, blank=True, null=True)


class Feedback(m.Model):  # Beware of SQLI
    user = m.ForeignKey(User, on_delete=m.CASCADE)
    page = m.SlugField()
    rate = m.BooleanField()
    desc = m.TextField(max_length=3000, blank=True, null=True)
    date = m.DateTimeField(auto_now_add=True)


class Thread(m.Model):
    id = m.BigAutoField(primary_key=True)
    user = m.ForeignKey(User, on_delete=m.CASCADE)
    cate = m.ForeignKey(Category, on_delete=m.PROTECT, null=True)
    open = m.BooleanField()


class Ticket(m.Model):  # Beware of SQLI
    id = m.BigAutoField(primary_key=True)
    thrd = m.ForeignKey(Thread, on_delete=m.CASCADE)
    text = m.TextField(max_length=5000)
    date = m.DateTimeField(auto_now_add=True)
    frmu = m.BooleanField()  # From Us
