from data.modelo.armas import Armas

class DaoArmas:
    def get_all(self, db) -> list[Armas]:
        cursor = db.cursor(dictionary=True)  # Agregamos dictionary=True
        cursor.execute("SELECT * FROM armas")
        armas_en_db = cursor.fetchall()
        
        armas = []
        for arma in armas_en_db:
            nueva_arma = Armas(
                arma["id"], arma["nombre"], arma["skin"], arma["precio"], arma["float_skin"], arma["stattrack"]
            )
            armas.append(nueva_arma)

        cursor.close()
        return armas


    def insert(self, db, nombre: str, skin: str, precio: float, float_skin: float, stattrack: bool):
        """Inserta una nueva arma en la base de datos"""
        cursor = db.cursor()
        sql = "INSERT INTO armas (nombre, skin, precio, float_skin, stattrack) VALUES (%s, %s, %s, %s, %s)"
        data = (nombre, skin, precio, float_skin, stattrack)
        cursor.execute(sql, data)
        db.commit()
        cursor.close()

    def update(self, db, id: int, nombre: str):
        cursor = db.cursor()
        sql = "UPDATE armas SET nombre = %s WHERE id = %s"  # Corregido
        data = (nombre, id)
        cursor.execute(sql, data)
        db.commit()
        cursor.close()

    
    def delete(self, db, id: int):
        """Elimina un arma por su ID"""
        cursor = db.cursor()
        sql = "DELETE FROM armas WHERE id = %s"
        cursor.execute(sql, (id,))
        db.commit()
        cursor.close()
