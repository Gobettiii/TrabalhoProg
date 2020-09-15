from config import *

class Telefone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    dd = db.Column(db.String(254))
    numero = db.Column(db.String(254))
    def __str__(self):
        return str(self.id)+")"+ self.nome + ", " + self.dd + self.numero 

    def json(self):
        return {
            "id": self.id,
            "nome" : self.nome,
            "dd" : self.dd,
            "numero" : self.numero
            
        }   
if __name__ == "__main__":

    if os.path.exists(arquivobd):
        os.remove(arquivobd)
    db.create_all()
    ex1 = Telefone(nome = "Lúcia", dd = "57", numero = "9999-9999")
    ex2 = Telefone(nome = "Antônio", dd = "11", numero = "1020-3040") 
    ex3 = Telefone(nome = "Fátima", dd = "48", numero = "9876-4567") 
    ex4 = Telefone(nome = "joão", dd = "69", numero = "1267-5424") 
    ex5 = Telefone(nome = "Ana", dd = "47", numero = "7939-1246")  
    db.session.add(ex1)
    db.session.add(ex2)
    db.session.add(ex3)
    db.session.add(ex4)
    db.session.add(ex5)
    db.session.commit()
    
    print(ex1.json())
    print(ex2.json())
    print(ex3.json())
    print(ex4.json())
    print(ex5.json())
