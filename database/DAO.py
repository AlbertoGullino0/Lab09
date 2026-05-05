from database.DB_connect import DBConnect
from model.Tratta import Tratta


class DAO():
    @staticmethod
    def getEdgePeso(avg):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        res = []
        query = """SELECT 
                        LEAST(ORIGIN_AIRPORT_ID, DESTINATION_AIRPORT_ID) AS a1,
                        GREATEST(ORIGIN_AIRPORT_ID, DESTINATION_AIRPORT_ID) AS a2,
                        AVG(DISTANCE) AS peso_medio
                    FROM flights
                    GROUP BY a1, a2
                    HAVING peso_medio > %s
                    order by peso_medio asc"""

        cursor.execute(query, (avg,))

        for row in cursor:
            res.append(Tratta(**row))

        cursor.close()
        conn.close()

        if len(res) == 0:
            return None

        return res

if __name__ == '__main__':
    DAO = DAO()
    result = DAO.getEdgePeso(4000)
    print(result)