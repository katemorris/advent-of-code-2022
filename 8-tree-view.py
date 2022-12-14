import code

with open("inputs/8.txt", "r") as file:
    rows = file.readlines()

tree_rows = {}
tree_columns = {}
row_num_map = len(rows)
for row in rows:
    row_trees = []
    for i, x in enumerate(row.strip()):
        row_trees.append(x)
        tree_columns.setdefault(f"{i}", []).insert(0, f"{x}")
    # print(row_num_map, row_trees)
    tree_rows[f"{row_num_map - 1}"] = row_trees
    row_num_map -= 1


def adjacent_tree_check(
    tree_value,
    row_max,
    col_max,
    tree_row,
    tree_col,
    row_app=0,
    col_app=0,
    count=0,
):
    # code.interact(local=dict(globals(), **locals()))
    while tree_row > 0 and tree_row < row_max and tree_col > 0 and tree_col < col_max:
        adj = tree_rows[str(tree_row + row_app)][tree_col + col_app]
        print(f"adjacent tree {adj} against {tree_value}")
        if adj < tree_value:
            count += 1
            return adjacent_tree_check(
                tree_value,
                row_max,
                col_max,
                (tree_row + row_app),
                (tree_col + col_app),
                row_app,
                col_app,
                count,
            )
        elif adj >= tree_value:
            count += 1
            return count
    return count


print(tree_rows)
# print(tree_columns)
row_num = len(tree_rows)
column_num = len(tree_columns)
most_viewed = 0
for row in range(row_num):
    row_str = str(row)
    if row in (0, row_num - 1):
        continue
    for column in range(column_num):
        print(f"coords ({row}, {column})")
        if column in (0, column_num - 1):
            continue
        tree = tree_rows[row_str][column]
        # check above
        print(f"checking above tree location ({row}, {column}) and value {tree}")
        above = adjacent_tree_check(
            tree, (row_num - 1), (column_num - 1), row, column, 1, 0
        )
        # check below
        print(f"checking below tree location ({row}, {column}) and value {tree}")
        below = adjacent_tree_check(
            tree, (row_num - 1), (column_num - 1), row, column, -1, 0
        )
        # check right
        # print(f"checking right of tree location ({row}, {column}) and value {tree}")
        right = adjacent_tree_check(
            tree, (row_num - 1), (column_num - 1), row, column, 0, 1
        )
        # check left
        # print(f"checking left of tree location ({row}, {column}) and value {tree}")
        left = adjacent_tree_check(
            tree, (row_num - 1), (column_num - 1), row, column, 0, -1
        )
        tree_view_count = above * below * right * left
        if tree_view_count > most_viewed:
            most_viewed = tree_view_count
print(most_viewed)
