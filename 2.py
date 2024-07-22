import pyspark.sql.functions as F

def get_product_category_pairs_and_products_without_categories(product_df, category_df, product_category_relation_df):
    
    product_category_joined_df = product_df.join(
        product_category_relation_df, on=F.col(product_df["product_id"]) == F.col(product_category_relation_df["product_id"])
    )

    product_category_df = product_category_joined_df.join(
        category_df, on=F.col(product_category_relation_df["category_id"]) == F.col(category_df["category_id"])
    )

    product_category_pairs_df = product_category_df.select(
        F.col(product_df["product_name"]).alias("product_name"),
        F.col(category_df["category_name"]).alias("category_name"),
    )

    product_with_categories_df = product_category_pairs_df.groupby("product_name")
    products_without_categories = product_with_categories_df.agg(F.count("category_name") == 0).alias("no_categories")

    products_without_categories_df = products_without_categories.filter(F.col("no_categories") == True)
    products_without_categories_list = products_without_categories_df.select("product_name").rdd.flatMap(lambda row: row).collect()

    return product_category_pairs_df, products_without_categories_list
