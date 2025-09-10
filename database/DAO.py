from database.DB_connect import DBConnect
from model.arco import Arco
from model.classification import Classification


class DAO():
    @staticmethod
    def getAllLocalizations():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select distinct c.Localization as localization
                        from classification c 
                        order by c.localization desc"""
            cursor.execute(query)

            for row in cursor:
                result.append(row["localization"])

            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def getAllNodes(localization):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select c.*
                        from classification c 
                        where c.Localization = %s"""

            cursor.execute(query,(localization,))

            for row in cursor:
                result.append(Classification(**row))

            cursor.close()
            cnx.close()
        return result


    @staticmethod
    def getAllEdges(localization, idMap):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select c1.GeneID as gene1, c2.GeneID as gene2, sum(distinct g.Chromosome) as peso
                        from classification c1, classification c2, interactions i, genes g
                        where c1.Localization = %s and c1.Localization = c2.Localization 
                        and c1.GeneID = i.GeneID1 and c2.GeneID = i.GeneID2 and c1.GeneID != c2.GeneID 
                        and (g.GeneID=c1.GeneID or g.GeneID=c2.GeneID)
                        group by c1.GeneID, c2.GeneID 
                        order by peso asc """
            cursor.execute(query,(localization,))

            for row in cursor:
                result.append(Arco(idMap[row["gene1"]], idMap[row["gene2"]], row["peso"]))

            cursor.close()
            cnx.close()
        return result



    ''''@staticmethod
    def get_all_genes():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT * 
                        FROM genes"""
            cursor.execute(query)

            for row in cursor:
                result.append(Gene(**row))

            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def get_all_interactions():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT * 
                           FROM interactions"""
            cursor.execute(query)

            for row in cursor:
                result.append(Interaction(**row))

            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def get_all_classifications():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT * 
                        FROM classification"""
            cursor.execute(query)

            for row in cursor:
                result.append(Classification(**row))

            cursor.close()
            cnx.close()
        return result '''
