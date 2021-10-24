import mysql.connector
from mysql.connector import errorcode
import usuario as user

class dbConnect():
  def connect(self):
    try:
      cnx = mysql.connector.connect(user='root', password='Invictus@2021',
                                    database='aps_6')
    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
      else:
        print(err)
    else:
      self.cnx = cnx
      return self

  def close(self):
      self.cnx.close()

  def getUser(self, email, senha, digital):
    self.cursor = self.cnx.cursor()
    query = ("SELECT nivel_acesso_id, ds_nome, ds_email, ds_senha, ds_digital FROM usuarios "
             "WHERE ds_email = %s AND ds_senha = %s AND ds_digital = %s")
    self.cursor.execute(query, (email, senha, digital))
    for (nivel_acesso, nome, email, senha, digital) in self.cursor:
      return user.Usuario(nivel_acesso, nome, email, senha, digital)
  
  def registerUser(self, nivel_acesso, nome, email, senha, digital):
    self.cursor = self.cnx.cursor()
    query = ("INSERT INTO usuarios VALUES (NULL, %s , %s , %s , %s , %s)")
    self.cursor.execute(query, (nivel_acesso, nome, email, senha, digital))
    self.cnx.commit()
    return user.Usuario(nivel_acesso, nome, email, senha, digital)

  def getFocoQueimadas(self):
    self.cursor = self.cnx.cursor()
    query = ("SELECT datahora,satelite,municipio,risco_fogo FROM foco_queimadas LIMIT 30;")
    self.cursor.execute(query)
    datahoraF,sateliteF,municipioF,risco_fogoF = '', '', '', ''
    for (datahora, satelite, municipio, risco_fogo) in self.cursor:
      datahoraF = datahoraF + str(datahora) + '\n'
      sateliteF = sateliteF + satelite + '\n'
      municipioF = municipioF + municipio + '\n'
      risco_fogoF = risco_fogoF + str(risco_fogo) + '\n'
    return [datahoraF,sateliteF,municipioF,risco_fogoF]