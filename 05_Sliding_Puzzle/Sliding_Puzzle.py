import psycopg2
import numpy as np


def list_to_string(list):
    output = ""
    if list.ndim == 2:
        output = list2d_to_string(list)
    elif list.ndim == 3:
        for dim in range(len(list)):
            output += list2d_to_string(list[dim]) + ";"
        output = output[:-1]
    return output


def list2d_to_string(list2d):
    output = ""
    for row in list2d:
        for col in row:
            output += str(col)
    return output


def string_to_np_array(string):
    data = [x for x in string]
    output = np.array(data, dtype=int)
    return output.reshape(3,3)


def drop_table_if_exsits(conn, table_name):
    try:
        cursor = conn.cursor()
        query = "DROP TABLE IF EXISTS " + table_name
        cursor.execute(query)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error Happen")
        print(query)
        print(error)
    finally:
        if cursor is not None:
            cursor.close()


def create_table_states(conn):
    try:
        cursor = conn.cursor()
        query = ""
        query += "CREATE TABLE states (                 " + "\n"
        query += "    id          SERIAL      NOT NULL, " + "\n"
        query += "    state       VARCHAR(9)  NOT NULL, " + "\n"
        query += "    actions     VARCHAR(9)          , " + "\n"
        query += "    next_states VARCHAR(39)         , " + "\n"
        query += "    next_ids    VARCHAR(27)           "
        query += ")                                     "
        cursor.execute(query)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error Happen")
        print(query)
        print(error)
    finally:
        if cursor is not None:
            cursor.close()


def check_state(conn, state):
    try:
        state_str = list_to_string(state)
        cursor = conn.cursor()
        query = "SELECT COUNT(state) FROM states WHERE state = %s"
        cursor.execute(query, (state_str,))
        tuple = cursor.fetchone()
        count = tuple[0]
        return count > 0
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error Happen")
        print(query)
        print(error)
    finally:
        if cursor is not None:
            cursor.close()


def insert_state(conn, state):
    try:
        cursor = None
        is_state_duplicated = check_state(conn, state)
        if is_state_duplicated is False:
            cursor = conn.cursor()
            state_str = list_to_string(state)
            query = "INSERT INTO states (state) VALUES (%s)"
            cursor.execute(query, (state_str,))
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error Happen")
        print(query)
        print(error)
    finally:
        if cursor is not None:
            cursor.close()


def find_next_id(conn):
    try:
        cursor = conn.cursor()
        query = ""
        query += "SELECT id FROM states       " + "\n"
        query += "WHERE                       " + "\n"
        query += "    state is NOT NULL       " + "\n"
        query += "    AND actions is NULL     " + "\n"
        query += "    AND next_states is NULL " + "\n"
        query += "ORDER BY id                 " + "\n"
        query += "LIMIT 1                     "
        cursor.execute(query)
        tuple = cursor.fetchone()
        if tuple is None:
            return None
        else:
            next_id = tuple[0]
            return next_id
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error Happen")
        print(query)
        print(error)
    finally:
        if cursor is not None:
            cursor.close()


def select_state_by_id(conn, id):
    try:
        cursor = conn.cursor()
        query = "SELECT state FROM states WHERE id ='" + str(id) + "'"
        cursor.execute(query)
        row = cursor.fetchone()
        output = string_to_np_array(row[0])
        return output
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error Happen")
        print(query)
        print(error)
    finally:
        if cursor is not None:
            cursor.close()


def update_actions_by_id_state(conn, actions, id):
    try:
        actions_str = list_to_string(actions)
        cursor = conn.cursor()
        query = ""
        query += "UPDATE states            " + "\n"
        query += "    SET actions = %s     " + "\n"
        query += "    WHERE id = %s        " + "\n"
        cursor.execute(query, (actions_str, id))
        conn.commit()
        # print("id =" + str(id) + " row's actions column is updated")
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error Happen")
        print(query)
        print(error)
    finally:
        if cursor is not None:
            cursor.close()


def update_next_state_by_id(conn, next_states, id):
    try:
        next_states_str = list_to_string(next_states)
        cursor = conn.cursor()
        query = ""
        query += "UPDATE states            " + "\n"
        query += "    SET next_states = %s " + "\n"
        query += "    WHERE id = %s        "
        cursor.execute(query, (next_states_str, id))
        conn.commit()
        # print("id =" + str(id) + " row's next_state column is updated")
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error Happen")
        print(query)
        print(error)
    finally:
        if cursor is not None:
            cursor.close()


def get_next_id_by_next_state(conn, next_state):
    next_state_str = list_to_string(next_state)
    try:
        cursor = conn.cursor()
        query = ""
        query += "SELECT id FROM states WHERE state = %s"
        cursor.execute(query, (next_state_str,))
        row = cursor.fetchone()
        next_id = row[0]
        return str(next_id)
    except (Exception, psycopg2.DatabaseError) as error:
        print(query)
        print("Error Happen")
        print(error)
    finally:
        if cursor is not None:
            cursor.close()


def update_next_id_by_id(conn, id, next_id_str):
    try:
        cursor = conn.cursor()
        query = ""
        query += "UPDATE states         " + "\n"
        query += "    SET next_ids = %s " + "\n"
        query += "    WHERE id = %s     " + "\n"
        cursor.execute(query, (next_id_str, id))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error Happen")
        print(query)
        print(error)
    finally:
        if cursor is not None:
            cursor.close()


def get_actions(state):
    i, j = get_target_number_position_list(state, 0)[0]
    data = np.ones(9)
    actions = np.array(data, dtype=int).reshape(3, 3)
    actions[i][j] = 0

    # upper
    if 0 <= i - 1 <= 2 and 0 <= j <= 2:
        actions[i-1][j] += 1
    # lower
    if 0 <= i + 1 <= 2 and 0 <= j <= 2:
        actions[i+1][j] += 1
    # left
    if 0 <= i <= 2 and 0 <= j - 1 <= 2:
        actions[i][j-1] += 1
    # right
    if 0 <= i <= 2 and 0 <= j + 1 <= 2:
        actions[i][j+1] += 1
    return actions


def get_target_number_position_list(state, target_num):
    output = []
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == target_num:
                output.append((i, j))
    return output


def get_next_states(state, actions):
    data = []
    zero_i, zero_j = get_target_number_position_list(state, 0)[0]
    for (action_i, action_j) in get_target_number_position_list(actions, 2):
        next_state = np.copy(state)
        next_state[zero_i][zero_j], next_state[action_i][action_j] = next_state[action_i][action_j], next_state[zero_i][zero_j]
        data = np.append(data, next_state)
    output = np.array(data, dtype=int).reshape(int(len(data)/9), 3, 3)
    return output


def pprint(data):
    print("type", type(data))
    print("dimension", data.ndim)
    print(data)


if __name__ == "__main__":
    # initial data
    last_state_list = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    last_state = np.array(last_state_list, dtype=int)
    last_state_str = list_to_string(last_state)
    last_state = string_to_np_array(last_state_str)

    # start
    conn =  psycopg2.connect("dbname='mydatabase' user='myuser' host='localhost' port='65432' password='123qwe'")

    # initial database
    drop_table_if_exsits(conn, "states")
    create_table_states(conn)
    insert_state(conn, last_state)

    # state search
    # find id
    id = 1
    while id is not None:
        # 1 state
        select_state = select_state_by_id(conn, id)

        # 2 actions
        actions = get_actions(select_state)
        # pprint(actions)
        update_actions_by_id_state(conn, actions, id)

        # 3 next_state
        next_states = get_next_states(select_state, actions)
        # pprint(next_states)
        update_next_state_by_id(conn, next_states, id)
        for new_state in next_states:
            insert_state(conn, new_state)

        # 4 next_id
        next_id_str = ""
        for next_state in next_states:
            next_id_str += get_next_id_by_next_state(conn, next_state) + ","
        update_next_id_by_id(conn, id, next_id_str[:-1])

        # 5 id
        id = find_next_id(conn)

    # end
    conn.close
