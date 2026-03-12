from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    error = None
    PRECIO_BOLETA = 12

    if request.method == 'POST':
        nombre = request.form.get('nombre')
        compradores = int(request.form.get('compradores'))
        boletas = int(request.form.get('boletas'))
        usa_cineco = request.form.get('cineco') == 'si'
        
        max_permitido = compradores * 7
        
        if boletas > max_permitido:
            error = f"No puede comprar más de 7 boletas por persona. El límite es {max_permitido}."
        else:
            subtotal = boletas * PRECIO_BOLETA
            descuento_boleta = 0
            
            if boletas > 5:
                descuento_boleta = 0.15
            elif boletas >= 3:
                descuento_boleta = 0.10
            
            total = subtotal * (1 - descuento_boleta)
            
            if usa_cineco:
                total *= 0.90
            
            resultado = {'nombre': nombre, 'total': total}
            
    return render_template('index.html', resultado=resultado, error=error)

if __name__ == '__main__':
    app.run(debug=True)