from django.contrib import admin
from .models import ProdukItem, OrderProdukItem, Order, AlamatPengiriman, Payment, Contact, Comment, Rating

class ProdukItemAdmin(admin.ModelAdmin):
    list_display = ['nama_produk','harga', 'harga_diskon', 'slug',
                    'deskripsi', 'gambar', 'label', 'kategori']

class OrderProdukItemAdmin(admin.ModelAdmin):
    list_display = ['user', 'ordered', 'produk_item', 'quantity']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'tanggal_mulai', 'tanggal_order', 'ordered']

class AlamatPengirimanAdmin(admin.ModelAdmin):
    list_display = ['user', 'alamat_1', 'alamat_2', 'kode_pos', 'negara']

class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount', 'timestamp', 'payment_option', 'charge_id']

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject']

class RatingAdmin(admin.ModelAdmin):
    list_display = ['user', 'produk', 'rating']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'produk', 'comment']



admin.site.register(ProdukItem, ProdukItemAdmin)
admin.site.register(OrderProdukItem, OrderProdukItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(AlamatPengiriman, AlamatPengirimanAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Comment, CommentAdmin)