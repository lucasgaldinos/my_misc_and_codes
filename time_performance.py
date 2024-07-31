
from time import perf_counter
import inspect


def time_perf(func):
    total_time = 0

    def wrapper(*args, **kwargs):
        nonlocal total_time
        t_start = perf_counter()
        result = func(*args, **kwargs)
        t_end = perf_counter()
        execution_time = t_end - t_start
        total_time += execution_time
        print(f"time: {execution_time}")
        return result

    def get_total_time():
        return total_time

    wrapper.get_total_time = get_total_time
    return wrapper


def my_time_it(func):
    """create wrapper for perf_counter"""
    def wrapper(*args, **kwargs):
        t1_start = perf_counter()
        result = func(*args, **kwargs)
        t1_end = perf_counter()
        print(f"{len(args[0])}, time: {t1_end - t1_start}")
        return result

    return wrapper

# t1_start = perf_counter()

# # code

# t1_end = perf_counter()
# print(f"{len(lista)}, time: {t1_end-t1_start}")

# Examples on deere
# @time_perf
# def process_data(
#     df: DataFrame, product: str, str_to_filter: str, join_column: str = "unique_id"
# ):  # (df: DataFrame, product: str, str_to_filter: str, column_to_filter: str)
#     """
#     # TO-DO: Must be implemented to va_03, not only dealer_export, by substituting also the column SUBCATEGORY"""
#     product_type = df.filter(col("SUBCATEGORY").rlike(str_to_filter)).orderBy(
#         "SUBCATEGORY"
#     ) # col(column_to_filter)....orderBy(column_to_filter)
#     print(f"{product} = {product_type.count()}")
#     new_df_name = df.join(
#         product_type, on=join_column, how="left_anti" # on = column_to_filter
#     ) # or this step is making the process take to long
#     new_df_name = new_df_name
#     del df
#     return new_df_name, product_type
