import psycopg2
import numpy as np
import json
import copy


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
    return output.reshape(3, 3)


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
        if cursor.closed is False:
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
        query += "    next_ids    VARCHAR(27)         , " + "\n"
        query += "    position    json                  " + "\n"
        query += ")                                     "
        cursor.execute(query)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error Happen")
        print(query)
        print(error)
    finally:
        if cursor.closed is False:
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
        if cursor.closed is False:
            cursor.close()


def insert_state_position(conn, state, position):
    try:
        cursor = conn.cursor()
        is_state_duplicated = check_state(conn, state)
        if is_state_duplicated is False:
            state_str = list_to_string(state)
            position_str = json.dumps(position)
            query = "INSERT INTO states (state, position) VALUES (%s, %s)"
            cursor.execute(query, (state_str, position_str))
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error Happen")
        print(query)
        print(error)
    finally:
        if cursor.closed is False:
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
        if cursor.closed is False:
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
        if cursor.closed is False:
            cursor.close()


def select_state_position_by_id(conn, id):
    try:
        cursor = conn.cursor()
        query = "SELECT state, position FROM states WHERE id = %s"
        cursor.execute(query, (id,))
        row = cursor.fetchone()
        select_state = string_to_np_array(row[0])
        select_position = row[1]
        return select_state, select_position
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error Happen")
        print(query)
        print(error)
    finally:
        if cursor.closed is False:
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
        if cursor.closed is False:
            cursor.close()


def update_next_states_by_id(conn, next_states, id):
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
        if cursor.closed is False:
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
        if cursor.closed is False:
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
        if cursor.closed is False:
            cursor.close()


def create_actions(state):
    i, j = create_target_number_position_list(state, 0)[0]
    data = np.ones(9)
    actions = np.array(data, dtype=int).reshape(3, 3)
    actions[i][j] = 0

    # upper
    if 0 <= i - 1 <= 2 and 0 <= j <= 2:
        actions[i - 1][j] += 1
    # lower
    if 0 <= i + 1 <= 2 and 0 <= j <= 2:
        actions[i + 1][j] += 1
    # left
    if 0 <= i <= 2 and 0 <= j - 1 <= 2:
        actions[i][j - 1] += 1
    # right
    if 0 <= i <= 2 and 0 <= j + 1 <= 2:
        actions[i][j + 1] += 1
    return actions


def create_target_number_position_list(state, target_num):
    output = []
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == target_num:
                output.append((i, j))
    return output


def create_next_states_next_positions(state, actions, position):
    data_states = []
    out_positions = []
    zero_i, zero_j = create_target_number_position_list(state, 0)[0]
    for (action_i, action_j) in create_target_number_position_list(actions, 2):
        # state
        tmp_state = np.copy(state)
        tmp_state[zero_i][zero_j], tmp_state[action_i][action_j] = tmp_state[action_i][action_j], tmp_state[zero_i][
            zero_j]
        data_states = np.append(data_states, tmp_state)
        # position
        tmp_position = copy.deepcopy(position)
        tmp_position["x"] += action_j - zero_j
        tmp_position["y"] += zero_i - action_i
        out_positions.append(tmp_position)
    out_states = np.array(data_states, dtype=int).reshape(int(len(data_states) / 9), 3, 3)
    return out_states, out_positions


def pprint(data):
    print("type", type(data))
    print("dimension", data.ndim)
    print(data)


def update_position_by_id(conn, id, position_json):
    try:
        cursor = conn.cursor()
        query = ""
        query += "UPDATE states         " + "\n"
        query += "    SET position = %s " + "\n"
        query += "    WHERE id = %s     " + "\n"
        cursor.execute(query, (json.dumps(position_json), id))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error Happen")
        print(query)
        print(error)
    finally:
        if cursor.closed is False:
            cursor.close()


if __name__ == "__main__":
    # initial data
    last_state_list = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    initial_state = np.array(last_state_list, dtype=int)
    initial_state_str = list_to_string(initial_state)
    initial_state = string_to_np_array(initial_state_str)
    initial_position = json.loads('{"x": 2, "y": 0, "reword": 0}')

    # start
    conn = psycopg2.connect("dbname='mydatabase' user='myuser' host='localhost' port='65432' password='123qwe'")

    # initial database
    drop_table_if_exsits(conn, "states")
    create_table_states(conn)
    insert_state_position(conn, initial_state, initial_position)

    # state search
    id = find_next_id(conn)
    while id is not None:
        # 1 state and position
        state, position = select_state_position_by_id(conn, id)

        # 2 actions
        actions = create_actions(state)
        # pprint(actions)
        update_actions_by_id_state(conn, actions, id)

        # 3 next_states
        next_states, next_positions = create_next_states_next_positions(state, actions, position)
        # pprint(next_states)
        update_next_states_by_id(conn, next_states, id)
        for i in range(len(next_states)):
            new_state = next_states[i]
            new_position = next_positions[i]
            insert_state_position(conn, new_state, new_position)

        # 4 next_id
        next_id_str = ""
        for next_state in next_states:
            next_id_str += get_next_id_by_next_state(conn, next_state) + ","
        update_next_id_by_id(conn, id, next_id_str[:-1])

        # 5 id
        id = find_next_id(conn)
        if id is not None and id % 10000 == 0:
            print(id)

    # end
    conn.close
