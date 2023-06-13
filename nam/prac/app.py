from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    user_name = "Nam"
    return render_template('index.html', user_name = user_name)

@app.route('/product')
def product():
    product_list = ["computer1", "computer2", "computer3"]
    product_dict = {"product_name":"computer1", "product_price":"4300", "product_maker":"maker1"}
    return render_template('product.html', products = product_list, product_dict = product_dict)

@app.errorhandler(404)
def error_404(error):
    return render_template('error_pages/404.html'), 404

# @app.route('/product/<product_id>')
# def product(product_id):
#     product_list = [
#         ["1", "ノートパソコンA", "Core i5", "￥68,500"],
#         ["2", "ノートパソコンB", "AMD Ryzen 5", "￥81,300"],
#         ["3", "ノートパソコンC", "CeleronN4020", "￥64,300"]
#     ]
#     for product in product_list:
#         if product_id in product:
#             break
#     product_name = product[1]
#     product_cpu = product[2]
#     product_price = product[3]
#     return 'product_name:{0} product_cpu:{1},product_name:{2}'.format(product_name,product_cpu,product_price)


if __name__ == '__main__':
    app.run(debug=True)