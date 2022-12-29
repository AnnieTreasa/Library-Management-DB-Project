
            return []
        else:
            return book
    except mysql.connector.Error as err:
        print(err)