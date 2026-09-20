
from pyscript import display, document
# reciept generator
def make_reicipt(e):
        document.getElementById("result").innerHTML = " "
        prod1 = document.getElementById("item1")
        prod2 = document.getElementById("item2")
        prod3 = document.getElementById("item3")
        prod4 = document.getElementById("item4")
        prod5 = document.getElementById("item5")
        prod6 = document.getElementById("item6")


        subtotal = float(prod1.value) * prod1.checked + float(prod2.value) * prod2.checked + float(prod3.value) * prod3.checked + float(prod4.value) * prod4.checked + float(prod5.value) * prod5.checked + float(prod6.value) * prod6.checked

        display(f'The subtotal is {subtotal}', target="result")

        vat_number = subtotal * 0.12
        display(f'The VAT is {vat_number}', target="result")

        total_amount = subtotal + vat_number
        display(f'The total amount is {total_amount}', target="result")

# sku generator

def generate_sku(e):

    category = document.getElementById("category")
    product = document.getElementById("product")
    stock = document.getElementById("stock")

    category_code = category.value
    product_name = product.value
    stock_quantity = stock.value

    product_code = product_name.upper()
    product_code = product_code.replace(" ", "")
    product_code = product_code[:4]

    sku = category_code + "-" + product_code + "-" + stock_quantity

    document.getElementById("result").textContent = sku