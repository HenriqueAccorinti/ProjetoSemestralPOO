import streamlit as st
import sqlite3
import time

#Models
class User():
    def __init__(self, name, email, password, cpf):
        self._email = email
        self._name = name
        self._password = password
        self._cpf = cpf

    def get_password(self):
        return self._password

    def get_name(self):
        return self._name

    def get_email(self):
        return self._email

    def get_cpf(self):
        return self._cpf

    def __str__(self)->str:
        return f'User(name:{self.get_name()}, email:{self.get_email()}, password:{self.get_password()} cpf:{self.get_cpf()}'

class Product():
    def __init__(self, name, price, url, amount):
        self._name = name
        self._price = price
        self._url = url
        self._amount = amount

    def get_name(self):
        return self._name
        
    def get_price(self):
        return self._price

    def get_url(self):
        return self._url
    
    def get_amount(self):
        return self._amount
    
    def set_amount(self, amount):
        self._amount = amount

    def __str__(self)->str:
        return f'Product(name:{self.get_name()}, price:{self.get_price()}, url:{self.get_url()}, amount:{self.get_amount()})'

class Cart():

    def __init__(self):
        self._products=[]

    def get_products(self):
        return self._products
    
    def set_products(self, products):
        self._products = products
        
    def __str__(self)->str:
        return self._products


#DAOs
class UserDAO():
    _instance = None
    
    def __init__(self) -> None:
        self._connect()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = UserDAO()
        return cls._instance

    def _connect(self):
        self.conn = sqlite3.connect(r'Ternos.db', check_same_thread=False)

    '''
    def create_tables(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Users (
                name TEXT,
                email TEXT,
                password TEXT,
                cpf TEXT
            );
        """)

        self.conn.commit()
        self.cursor.close()
    '''    

    def get_all(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            SELECT * FROM Users;
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(User(name = resultado[1], email = resultado[2], password = resultado[3], cpf = resultado[4]))
        self.cursor.close()
        return resultados

    def inserir_user(self, user):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            INSERT INTO Users(name, email, password, cpf)
            Values(?,?,?,?);
        """, (user.get_name(), user.get_email(), user.get_password(),user.get_cpf()))
        self.conn.commit()
        self.cursor.close()

    def pegar_user(self, email):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Users
            WHERE email = '{email}';
        """)
        user  = None
        resultado = self.cursor.fetchone()
        if resultado != None:
            user = (User(name = resultado[1], email = resultado[2], password = resultado[3], cpf = resultado[4]))
        self.cursor.close()
        return user

    def atualizar_user(self, user):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                UPDATE Users SET
                email = '{user.get_email()}',
                password = '{user.get_password()}'
                WHERE cpf = '{user.get_cpf()}'
                
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True
    
    def deletar_user(self, email):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                DELETE FROM Users 
                WHERE email = '{email}'
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True
    
    def search_all_for_name(self, name):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Users
            WHERE name LIKE '{name}%';
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(User(name = resultado[1], email = resultado[2], password = resultado[3], cpf = resultado[4]))
        self.cursor.close()
        return resultados

class ProductDAO():
    _instance = None
    
    def __init__(self) -> None:
        self._connect()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = ProductDAO()
        return cls._instance

    def _connect(self):
        self.conn = sqlite3.connect(r'Ternos.db', check_same_thread=False)

    def get_all(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            SELECT * FROM Products;
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(Product(name = resultado[0], price = resultado[1], url = resultado[2], amount = resultado[3]))
        self.cursor.close()
        return resultados

    '''
    def deleteProducts(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            DELETE FROM Products;
        """)

        self.conn.commit()
        self.cursor.close()
    '''
    
    def inserir_product(self, product):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                INSERT INTO Products (name, price, url, amount)
                Values(?,?,?,?);
            """, (product.get_name(), product.get_price(), product.get_url(),product.get_amount()))

            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True

    def pegar_product(self, name):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Products
            WHERE name = '{name}';
        """)
        product  = None
        resultado = self.cursor.fetchone()
        if resultado != None:
            product = (Product(name = resultado[0], price = resultado[1], url = resultado[2], amount = resultado[3]))
        self.cursor.close()
        return product

    def atualizar_product(self, product):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                UPDATE Products SET
                amount = '{product.get_amount()}'
                WHERE name = '{product.get_name()}'
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True
    
    def deletar_product(self, email):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                DELETE FROM Products 
                WHERE email = '{email}'
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True
    
    def search_all_for_name(self, name):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Products
            WHERE name LIKE '{name}%';
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(Product(name = resultado[0], price = resultado[1], url = resultado[2], amount = resultado[3]))
        self.cursor.close()
        return resultados


#Controllers
class UserController():
    def __init__(self):
        # Carrega os dados dos usuários
        # self._products = UserDAO.get_instance().create_tables()
        self._users = UserDAO.get_instance().get_all()

    def check_login(self, email, password):
        user_t = {}
        for user in self._users:
            user_email = user.get_email()
            passw = user.get_password()
            user_t[user_email] = (passw, [user.get_name(), user.get_cpf()])

        try:
            if user_t[email][0] == password:
                st.session_state["Login"] = "aprovado"
                st.session_state['Usuario'] = user_t[email][1][0] # Nome
                st.session_state['Cpf'] = user_t[email][1][1]     # CPF
                st.session_state['Email'] = email                 # Email
                
            else:
                st.session_state["Login"] = "errado"

        except KeyError:

            st.session_state["Login"] = "errado"
            

    def sign_up(self, name, email, password, cpf):
        user = User(name, email, password, cpf)
       
        try:
            UserDAO.get_instance().inserir_user(user)
            st.success("Registrado")
            st.session_state["Login"] = "negado"
        except:
            st.error("Email ou cpf já registrados")

    def logout():
        st.session_state["Login"] = "negado"
        st.session_state["Cart"] = CartController()
    
    def change_data(self, email, password):
        user = User(st.session_state['Usuario'], email, password, st.session_state['Cpf'])
        try:
            UserDAO.get_instance().atualizar_user(user)
            st.success("Alterado com Sucesso")
            st.session_state["Profile"] = "dados"
            st.session_state['Email'] = user.get_email()
        except:
            st.error("Email já registrado")
    
    def change_login():
        st.session_state["Profile"] = "change"

    def go_back():
        st.session_state["Profile"] = "dados"
    
    def sign_up_screen():
        st.session_state["Login"] = "registro"
    
    def login_screen():
        st.session_state["Login"] = "negado"
    
    def home_screen():
        st.session_state["Login"] = "negado"
        time.sleep(0.2)
        st.session_state["Login"] = "aprovado"

class ProductController():
    def __init__(self):
        #self._products = ProductDAO.get_instance().deleteProducts()
        self._products = ProductDAO.get_instance().get_all()

    def get_product(self,index):
        return self._products[index]
    
    def get_products(self):
        return self._products

    def sign_product(self, name, price, url, amount):
        product = Product(name, price, url, amount)

        product_test = ProductDAO.get_instance().inserir_product(product)
        if product_test == False:
            st.session_state["carrinho"] = "Falha ao Cadastrar"
            print(product_test)
        else:
            st.session_state["carrinho"] = "Produto Cadastrado Com Sucesso"
            st.session_state["Login"] = "negado"
            time.sleep(0.2)
            st.session_state["Login"] = "aprovado"
    
    def update_product(self, amount, name):
       up_product = ProductDAO.get_instance().atualizar_product(amount, name)
       if up_product == False:
           st.session_state["carrinho"] = "Falha ao Editar"
           print(up_product)
       else:
           st.session_state["carrinho"] = "Produto Editado Com Sucesso"
           st.session_state["Login"] = "negado"
           time.sleep(0.2)
           st.session_state["Login"] = "aprovado"

class CartController():
    def __init__(self):
        self._cart = Cart()

    def get_cart(self):
        return self._cart

    def add_product(self,product,quantity):
        for i in range(len(self.get_cart().get_products())):
            if self.get_cart().get_products()[i][0].get_name() == product.get_name() and quantity <= product.get_amount():
                if self.get_cart().get_products()[i][1] + quantity <= product.get_amount():
                    self.get_cart().get_products()[i][1] += quantity
                    st.session_state["falta"] = ""

                else:
                    st.session_state["falta"] = f"{product.get_name()} tem somente {product.get_amount()} unidade(s) disponível(is) em estoque"
                return
        self.get_cart().get_products().append([product,quantity])

    def get_total_price(self):
        total = 0
        for items in self.get_cart().get_products():
            total += items[0].get_price() * items[1]
        return total

    def clear_cart(self):
        try:
            for item in self.get_cart().get_products():
                if item[0].get_amount() - item[1] >= 0:
                    item[0].set_amount(item[0].get_amount() - item[1])
                ProductDAO.get_instance().atualizar_product(item[0])
            self.get_cart().set_products([])
            return True
        except:
            return False


p_controller = ProductController()

st.set_page_config(page_title="Ternos.com", page_icon="👔")

image_urls = [
'https://images.unsplash.com/photo-1532207733185-fc73ca0a54b5?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1917&q=80',
'https://images.unsplash.com/photo-1580656940647-8854a00547f0?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80',
'https://images.unsplash.com/photo-1521485714898-f097eb6fc5b9?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80',
'https://images.unsplash.com/photo-1585412459212-8def26f7e84c?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1935&q=80',
'https://images.unsplash.com/photo-1491336477066-31156b5e4f35?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80',
'https://images.unsplash.com/photo-1600091166971-7f9faad6c1e2?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1887&q=80',
'https://images.unsplash.com/photo-1507679799987-c73779587ccf?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2071&q=80',
'https://images.unsplash.com/photo-1580657018950-c7f7d6a6d990?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80'
]

if "Login" not in st.session_state:
    st.session_state["Profile"] = "dados"
    st.session_state["Login"] = "negado"
    st.session_state["Usuario"] = ""
    st.session_state["email"] = ""
    st.session_state["falta"] = ""
    st.session_state["Cart"] = CartController()
    st.session_state["carrinho"] = ""


    for image_url in image_urls:
        st.image(image_url, width=700)
    st.markdown("Faça seu Login no canto esquerdo da tela para utilizar nossos serviços!")

    
with st.sidebar:

    if st.session_state["Login"] == "negado" or st.session_state["Login"] == "errado":

        st.title("Bem vindo!")
        st.markdown("Faça seu Login para utilizar nossos serviços!")
        st.divider()

        email = st.text_input(
            label="Email",
            placeholder= "Digite seu email"
        )

        password = st.text_input(
            label="Senha",
            placeholder= "Digite sua senha",
            type = "password"
        )
        
        col1, col2 = st.columns(2)

        with col1:
            st.button(label= "Entrar", on_click= UserController.check_login, args = (UserController(),email,password))

        with col2:
            st.button(label = "Registrar-se", on_click = UserController.sign_up_screen)
    
    if st.session_state['Login'] == 'errado':
        st.warning("Email ou senha incorretos!")
        
    if st.session_state["Login"] == "registro":
        st.title("Cadastro")

        name = st.text_input(
            label="Nome",
            key = 1,
            placeholder= "Digite seu nome"
        )

        email = st.text_input(
            label="Email",
            key = 2,
            placeholder= "Digite seu email"
        )

        password = st.text_input(
            label="Senha",
            type = "password",
            key = 3,
            placeholder= "Digite sua senha"
        )

        cpf = st.text_input(
            label="CPF",
            key = 4,
            placeholder= "Digite seu cpf"
        )

        col1, col2 = st.columns(2)

        with col1:
            st.button(
                label= "Voltar", 
                on_click= UserController.login_screen
            )

        with col2:
            st.button(
                label= "Cadastrar-se", 
                on_click= UserController.sign_up, 
                args = (UserController(),name, email, password, cpf)
            )

    if st.session_state["Login"] == "aprovado":

        st.title("Bem vindo a Ternos.com!👔")

if "Login" in st.session_state:

    if st.session_state["Login"] == "aprovado" and st.session_state["Email"] == "henrique@gmail.com":
        tab1, tab2, tab3, tab4 = st.tabs(["🏠 | Home", "🛒 | Carrinho", "➕ | Cadastrar Produtos", "➕ | Estoque"])

        with st.sidebar: 
            
            if st.session_state["Profile"] == "dados":
                st.markdown(f"Nome: {st.session_state['Usuario']}")
                st.markdown(f"Email: {st.session_state['Email']}")
                st.markdown(f"CPF: {st.session_state['Cpf']}")

                st.button(
                    label="Mudar informações de login", 
                    key= 7852084,
                    on_click= UserController.change_login
                )

                st.button(label= "Sair", on_click= UserController.logout)

            if st.session_state["Profile"] == "change":

                email = st.text_input(
                    label="Email",
                    key = 10000,
                    placeholder="Digite seu novo email"
                )

                password = st.text_input(
                    label="Senha",
                    type = "password",
                    key = 323,
                    placeholder="Digite sua nova senha"
                )

                col3, col4 = st.columns(2)

                with col3:
                    st.button(
                        label = "Voltar",
                        key = 99785, 
                        on_click = UserController.go_back
                    )
                
                with col4:
                    st.button(
                        label= "Alterar", 
                        key = 1234675, 
                        on_click= UserController.change_data, 
                        args = (UserController(), email, password)
                    )
                
        with tab1:

            col1,col2 = st.columns(2,gap="large")
            
            if st.session_state["falta"]:
                st.warning(st.session_state["falta"])
            
            for i in range(0, len(p_controller.get_products()) - 1, 2):
                with col1:

                    product = p_controller.get_product(index = i)
                    cont = st.container()
                    cont.markdown(f"{product.get_name()}")
                    try:
                        cont.image(f"{product.get_url()}", width=250)
                    except:
                        st.warning("Não foi possível carregar a imagem")

                    cont.markdown(f"R${product.get_price():.2f}")
                    quantity1 = cont.number_input(
                        label = "", 
                        key = 100 * (i+1), 
                        format = "%i", 
                        step = 1,
                        min_value = 1, 
                        max_value = product.get_amount() + 1
                    )
                    
                    if product.get_amount() > 0 and product.get_amount() - quantity1 >= 0:
                        cont.button(
                            label = f"Adicionar {product.get_name()}", 
                            key = 200 * (i+12), 
                            on_click= st.session_state["Cart"].add_product, 
                            args = (product, quantity1)
                        
                        )
                    else:
                        cont.markdown("Produto indisponivel")

                with col2:

                    product = p_controller.get_product(index = i + 1)
                    cont = st.container()
                    cont.markdown(f"{product.get_name()}")
                    try:
                        cont.image(f"{product.get_url()}",width=250)
                    except:
                        st.warning("Não foi possível carregar a imagem")

                    cont.markdown(f"R${product.get_price():.2f}")
                    quantity2 = cont.number_input(
                        label = "",  
                        format = "%i", 
                        key = 300 * (i+83), 
                        step = 1,
                        min_value = 1, 
                        max_value = product.get_amount()
                    )
                    
                    if product.get_amount() > 0 and product.get_amount() - quantity2 >= 0:    
                        cont.button(
                            label = f"Adicionar {product.get_name()}", 
                            key = 400 * (i+99), 
                            on_click= st.session_state["Cart"].add_product, 
                            args = (product, quantity2)
                        
                        )
                    else:
                        cont.warning("Produto indisponivel")

        with tab2:

            col1, col2, col3 = st.columns(3,gap="large")

            col1.title("Produto")
            col2.title("Preço")
            col3.title("Quantidade")
             
            product_qtt = []
            product_names = []
            product_prices = []

            for produquantity in st.session_state["Cart"].get_cart().get_products():

                product_names.append(produquantity[0].get_name())
                product_prices.append(produquantity[0].get_price())
                product_qtt.append(produquantity[1])
                    
            with col1:

                cont = st.container()
                for i in range(len(product_names)):
                    cont.markdown(f"{product_names[i]}")

            with col2:

                cont = st.container()
                for i in range(len(product_names)):
                    cont.markdown(f"R${product_prices[i]:.2f}")

            with col3:
                
                cont = st.container()
                for i in range(len(product_names)):
                    cont.markdown(f"{product_qtt[i]}")

            valor_total = st.session_state["Cart"].get_total_price()
            
            st.title(f"Valor total: R${valor_total:.2f} ")
            st.button(
                label = "Finalizar Pedido", 
                key = 998, 
                on_click= st.session_state["Cart"].clear_cart
            )
        
        with tab3:

            st.title("Cadastrar Produtos")
            
            name1 = st.text_input(
                label= "Nome",
                key = 2222,
                placeholder="Digite o nome do produto"
            )

            price1 = st.number_input(
                label="Preço",
                min_value=0,
                key = 4444
            )

            url1 = st.text_input(
                label="URL Da Imagem",
                key = 55555,
                placeholder="Digite o url da imagem do produto"
            )

            amount1 = st.number_input(
                label = "Quantidade",
                min_value=0,
                step=1,
                key = 66666
            )

            st.button(
                label= "Cadastrar produto", 
                on_click= ProductController.sign_product, 
                args = (ProductController(), name1, price1, url1, amount1)
            
            )
            st.markdown(st.session_state["carrinho"])

        with tab4:

            st.title("Editar Produtos")

            name2 = st.text_input(
                label= "Nome",
                key = 194,
                placeholder="Digite o nome do produto"
            )

            amount2 = st.number_input(
                label = "Quantidade",
                min_value=0,
                step=1,
                key = 195
            )

            st.button(
                label= "Editar produto", 
                on_click= ProductController.update_product, 
                args = (ProductController(), amount2, name2)
            )

            st.markdown(st.session_state["carrinho"])
    elif st.session_state["Login"] == "aprovado" and st.session_state["Email"] != "henrique@gmail.com":
        tab1, tab2 = st.tabs(["🏠 | Home", "🛒 | Carrinho"])
        with st.sidebar:
            if st.session_state["Profile"] == "dados":
                    st.markdown(f"Nome: {st.session_state['Usuario']}")
                    st.markdown(f"Email: {st.session_state['Email']}")
                    st.markdown(f"CPF: {st.session_state['Cpf']}")

                    st.button(
                        label="Mudar informações de login", 
                        key= 7852084,
                        on_click= UserController.change_login
                    )

                    st.button(label= "Sair", on_click= UserController.logout)

            if st.session_state["Profile"] == "change":

                email = st.text_input(
                    label="Email",
                    key = 10000,
                    placeholder="Digite seu novo email"
                )

                password = st.text_input(
                    label="Senha",
                    type = "password",
                    key = 323,
                    placeholder="Digite sua nova senha"
                )
                
                col3, col4 = st.columns(2)

                with col3:
                    st.button(
                        label = "Voltar",
                        key = 99785, 
                        on_click = UserController.go_back
                    )
                
                with col4:
                    st.button(
                        label= "Alterar", 
                        key = 1234675, 
                        on_click= UserController.change_data, 
                        args = (UserController(), email, password)
                    )

        with tab1:

            col1,col2 = st.columns(2,gap="large")
            
            if st.session_state["falta"]:
                st.warning(st.session_state["falta"])
            
            for i in range(0, len(p_controller.get_products()) - 1, 2):
                with col1:

                    product = p_controller.get_product(index = i)
                    cont = st.container()
                    cont.markdown(f"{product.get_name()}")
                    try:
                        cont.image(f"{product.get_url()}", width=250)
                    except:
                        st.warning("Não foi possível carregar a imagem")

                    cont.markdown(f"R${product.get_price():.2f}")
                    quantity1 = cont.number_input(
                        label = "", 
                        key = 100 * (i+1), 
                        format = "%i", 
                        step = 1,
                        min_value = 1, 
                        max_value = product.get_amount()
                    )
                    
                    if product.get_amount() > 0 and product.get_amount() - quantity1 >= 0:
                        cont.button(
                            label = f"Adicionar {product.get_name()}", 
                            key = 200 * (i+12), 
                            on_click= st.session_state["Cart"].add_product, 
                            args = (product, quantity1)
                        
                        )
                    else:
                        cont.markdown("Produto indisponivel")

                with col2:

                    product = p_controller.get_product(index = i + 1)
                    cont = st.container()
                    cont.markdown(f"{product.get_name()}")
                    try:
                        cont.image(f"{product.get_url()}",width=250)
                    except:
                        st.warning("Não foi possível carregar a imagem")

                    cont.markdown(f"R${product.get_price():.2f}")
                    quantity2 = cont.number_input(
                        label = "",  
                        format = "%i", 
                        key = 300 * (i+83), 
                        step = 1,
                        min_value = 1, 
                        max_value = product.get_amount()
                    )
                    
                    if product.get_amount() > 0 and product.get_amount() - quantity2 >= 0:    
                        cont.button(
                            label = f"Adicionar {product.get_name()}", 
                            key = 400 * (i+99), 
                            on_click= st.session_state["Cart"].add_product, 
                            args = (product, quantity2)
                        
                        )
                    else:
                        cont.warning("Produto indisponivel")

        with tab2:

            col1, col2, col3 = st.columns(3,gap="large")

            col1.title("Produto")
            col2.title("Preço")
            col3.title("Quantidade")
             
            product_qtt = []
            product_names = []
            product_prices = []

            for produquantity in st.session_state["Cart"].get_cart().get_products():

                product_names.append(produquantity[0].get_name())
                product_prices.append(produquantity[0].get_price())
                product_qtt.append(produquantity[1])
                    
            with col1:

                cont = st.container()
                for i in range(len(product_names)):
                    cont.markdown(f"{product_names[i]}")

            with col2:

                cont = st.container()
                for i in range(len(product_names)):
                    cont.markdown(f"R${product_prices[i]:.2f}")

            with col3:
                
                cont = st.container()
                for i in range(len(product_names)):
                    cont.markdown(f"{product_qtt[i]}")

            valor_total = st.session_state["Cart"].get_total_price()
            
            st.title(f"Valor total: R${valor_total:.2f} ")
            st.button(
                label = "Finalizar Pedido", 
                key = 998, 
                on_click= st.session_state["Cart"].clear_cart
            )