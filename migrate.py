from sqlalchemy import text
from app.config.connections import get_connection


with get_connection() as conn:
    conn.execute(
        text(
            """
            CREATE TABLE IF NOT EXISTS public.fraud_details (
                transaction_id int4 NOT NULL PRIMARY KEY,
                "day" float8 NOT NULL,
                "time" float8 NOT NULL,
                day_of_week float8 NOT NULL,
                day_of_month float8 NOT NULL,
                score float8 NOT NULL,
                "R_emaildomain" text NULL,
                "P_emaildomain" text NULL,
                id_30 text NULL,
                id_31 text NULL,
                id_33 text NULL,
                "DeviceInfo" text NULL,
                "ProductCD" text NULL,
                card4 text NULL,
                card6 text NULL,
                "M1" text NULL,
                "M2" text NULL,
                "M3" text NULL,
                "M4" text NULL,
                "M5" text NULL,
                "M6" text NULL,
                "M7" text NULL,
                "M8" text NULL,
                "M9" text NULL,
                id_12 text NULL,
                id_15 text NULL,
                id_16 text NULL,
                id_23 text NULL,
                id_27 text NULL,
                id_28 text NULL,
                id_29 text NULL,
                id_34 text NULL,
                id_35 text NULL,
                id_36 text NULL,
                id_37 text NULL,
                id_38 text NULL,
                "DeviceType" text NULL,
                pca0 float8 NOT NULL,
                pca1 float8 NOT NULL,
                pca2 float8 NOT NULL,
                pca3 float8 NOT NULL,
                pca4 float8 NOT NULL,
                pca5 float8 NOT NULL,
                pca6 float8 NOT NULL,
                pca7 float8 NOT NULL,
                pca8 float8 NOT NULL,
                pca9 float8 NOT NULL,
                pca10 float8 NOT NULL,
                pca11 float8 NOT NULL,
                pca12 float8 NOT NULL,
                pca13 float8 NOT NULL,
                pca14 float8 NOT NULL,
                pca15 float8 NOT NULL,
                pca16 float8 NOT NULL,
                pca17 float8 NOT NULL,
                pca18 float8 NOT NULL,
                pca19 float8 NOT NULL,
                pca20 float8 NOT NULL,
                pca21 float8 NOT NULL,
                pca22 float8 NOT NULL,
                pca23 float8 NOT NULL,
                pca24 float8 NOT NULL,
                pca25 float8 NOT NULL,
                pca26 float8 NOT NULL,
                pca27 float8 NOT NULL,
                pca28 float8 NOT NULL,
                pca29 float8 NOT NULL,
                pca30 float8 NOT NULL,
                pca31 float8 NOT NULL,
                pca32 float8 NOT NULL,
                pca33 float8 NOT NULL,
                pca34 float8 NOT NULL,
                pca35 float8 NOT NULL,
                pca36 float8 NOT NULL,
                pca37 float8 NOT NULL,
                pca38 float8 NOT NULL,
                pca39 float8 NOT NULL,
                pca40 float8 NOT NULL,
                pca41 float8 NOT NULL,
                pca42 float8 NOT NULL,
                pca43 float8 NOT NULL,
                pca44 float8 NOT NULL,
                pca45 float8 NOT NULL,
                pca46 float8 NOT NULL,
                pca47 float8 NOT NULL,
                pca48 float8 NOT NULL,
                pca49 float8 NOT NULL,
                pca50 float8 NOT NULL,
                pca51 float8 NOT NULL,
                pca52 float8 NOT NULL,
                pca53 float8 NOT NULL,
                pca54 float8 NOT NULL,
                pca55 float8 NOT NULL,
                pca56 float8 NOT NULL,
                pca57 float8 NOT NULL,
                pca58 float8 NOT NULL,
                pca59 float8 NOT NULL,
                pca60 float8 NOT NULL,
                pca61 float8 NOT NULL,
                pca62 float8 NOT NULL,
                pca63 float8 NOT NULL,
                pca64 float8 NOT NULL,
                pca65 float8 NOT NULL,
                pca66 float8 NOT NULL,
                pca67 float8 NOT NULL,
                pca68 float8 NOT NULL,
                pca69 float8 NOT NULL,
                pca70 float8 NOT NULL,
                pca71 float8 NOT NULL,
                pca72 float8 NOT NULL,
                pca73 float8 NOT NULL,
                pca74 float8 NOT NULL,
                pca75 float8 NOT NULL,
                pca76 float8 NOT NULL,
                pca77 float8 NOT NULL,
                pca78 float8 NOT NULL,
                pca79 float8 NOT NULL,
                pca80 float8 NOT NULL,
                pca81 float8 NOT NULL,
                pca82 float8 NOT NULL,
                pca83 float8 NOT NULL,
                pca84 float8 NOT NULL,
                pca85 float8 NOT NULL,
                pca86 float8 NOT NULL,
                pca87 float8 NOT NULL,
                pca88 float8 NOT NULL,
                pca89 float8 NOT NULL,
                pca90 float8 NOT NULL,
                pca91 float8 NOT NULL,
                pca92 float8 NOT NULL,
                pca93 float8 NOT NULL,
                pca94 float8 NOT NULL,
                pca95 float8 NOT NULL,
                pca96 float8 NOT NULL,
                pca97 float8 NOT NULL,
                pca98 float8 NOT NULL,
                pca99 float8 NOT NULL,
                pca100 float8 NOT NULL,
                pca101 float8 NOT NULL,
                pca102 float8 NOT NULL,
                pca103 float8 NOT NULL,
                pca104 float8 NOT NULL,
                pca105 float8 NOT NULL,
                pca106 float8 NOT NULL,
                pca107 float8 NOT NULL,
                pca108 float8 NOT NULL,
                pca109 float8 NOT NULL,
                pca110 float8 NOT NULL,
                pca111 float8 NOT NULL,
                pca112 float8 NOT NULL,
                pca113 float8 NOT NULL,
                pca114 float8 NOT NULL,
                pca115 float8 NOT NULL,
                pca116 float8 NOT NULL,
                pca117 float8 NOT NULL,
                "fe_R_emaildomain" float8 NOT NULL,
                "fe_P_emaildomain" float8 NOT NULL,
                fe_id_30 float8 NOT NULL,
                fe_id_31 float8 NOT NULL,
                fe_id_33 float8 NOT NULL,
                "fe_DeviceInfo" float8 NOT NULL,
                "ProductCD_H" float8 NOT NULL,
                "ProductCD_R" float8 NOT NULL,
                "ProductCD_S" float8 NOT NULL,
                "ProductCD_W" float8 NOT NULL,
                card4_discover float8 NOT NULL,
                card4_mastercard float8 NOT NULL,
                card4_visa float8 NOT NULL,
                card4_nan float8 NOT NULL,
                card6_credit float8 NOT NULL,
                card6_debit float8 NOT NULL,
                "card6_debit or credit" float8 NOT NULL,
                card6_nan float8 NOT NULL,
                "M1_T" float8 NOT NULL,
                "M1_nan" float8 NOT NULL,
                "M2_T" float8 NOT NULL,
                "M2_nan" float8 NOT NULL,
                "M3_T" float8 NOT NULL,
                "M3_nan" float8 NOT NULL,
                "M4_M1" float8 NOT NULL,
                "M4_M2" float8 NOT NULL,
                "M4_nan" float8 NOT NULL,
                "M5_T" float8 NOT NULL,
                "M5_nan" float8 NOT NULL,
                "M6_T" float8 NOT NULL,
                "M6_nan" float8 NOT NULL,
                "M7_T" float8 NOT NULL,
                "M7_nan" float8 NOT NULL,
                "M8_T" float8 NOT NULL,
                "M8_nan" float8 NOT NULL,
                "M9_T" float8 NOT NULL,
                "M9_nan" float8 NOT NULL,
                "id_12_NotFound" float8 NOT NULL,
                id_12_nan float8 NOT NULL,
                "id_15_New" float8 NOT NULL,
                "id_15_Unknown" float8 NOT NULL,
                id_15_nan float8 NOT NULL,
                "id_16_NotFound" float8 NOT NULL,
                id_16_nan float8 NOT NULL,
                "id_23_IP_PROXY:HIDDEN" float8 NOT NULL,
                "id_23_IP_PROXY:TRANSPARENT" float8 NOT NULL,
                id_23_nan float8 NOT NULL,
                "id_27_NotFound" float8 NOT NULL,
                id_27_nan float8 NOT NULL,
                "id_28_New" float8 NOT NULL,
                id_28_nan float8 NOT NULL,
                "id_29_NotFound" float8 NOT NULL,
                id_29_nan float8 NOT NULL,
                "id_34_match_status:0" float8 NOT NULL,
                "id_34_match_status:1" float8 NOT NULL,
                "id_34_match_status:2" float8 NOT NULL,
                id_34_nan float8 NOT NULL,
                "id_35_T" float8 NOT NULL,
                id_35_nan float8 NOT NULL,
                "id_36_T" float8 NOT NULL,
                id_36_nan float8 NOT NULL,
                "id_37_T" float8 NOT NULL,
                id_37_nan float8 NOT NULL,
                "id_38_T" float8 NOT NULL,
                id_38_nan float8 NOT NULL,
                "DeviceType_mobile" float8 NOT NULL,
                "DeviceType_nan" float8 NOT NULL,
                id_01 float8 NOT NULL,
                id_02 float8 NOT NULL,
                id_03 float8 NOT NULL,
                id_04 float8 NOT NULL,
                id_05 float8 NOT NULL,
                id_06 float8 NOT NULL,
                id_07 float8 NOT NULL,
                id_08 float8 NOT NULL,
                id_09 float8 NOT NULL,
                id_10 float8 NOT NULL,
                id_11 float8 NOT NULL,
                id_13 float8 NOT NULL,
                id_14 float8 NOT NULL,
                id_17 float8 NOT NULL,
                id_18 float8 NOT NULL,
                id_19 float8 NOT NULL,
                id_20 float8 NOT NULL,
                id_21 float8 NOT NULL,
                id_24 float8 NOT NULL,
                id_25 float8 NOT NULL,
                id_26 float8 NOT NULL,
                id_32 float8 NOT NULL,
                "TransactionAmt" float8 NOT NULL,
                card1 float8 NOT NULL,
                card2 float8 NOT NULL,
                card3 float8 NOT NULL,
                card5 float8 NOT NULL,
                addr1 float8 NOT NULL,
                addr2 float8 NOT NULL,
                dist1 float8 NOT NULL,
                dist2 float8 NOT NULL,
                "C1" float8 NOT NULL,
                "C2" float8 NOT NULL,
                "C3" float8 NOT NULL,
                "C4" float8 NOT NULL,
                "C6" float8 NOT NULL,
                "C7" float8 NOT NULL,
                "C8" float8 NOT NULL,
                "C9" float8 NOT NULL,
                "C10" float8 NOT NULL,
                "C11" float8 NOT NULL,
                "C12" float8 NOT NULL,
                "C13" float8 NOT NULL,
                "C14" float8 NOT NULL,
                "D1" float8 NOT NULL,
                "D3" float8 NOT NULL,
                "D4" float8 NOT NULL,
                "D6" float8 NOT NULL,
                "D7" float8 NOT NULL,
                "D8" float8 NOT NULL,
                "D9" float8 NOT NULL,
                "D10" float8 NOT NULL,
                "D11" float8 NOT NULL,
                "D12" float8 NOT NULL,
                "D13" float8 NOT NULL,
                "D14" float8 NOT NULL,
                created_at timestamp DEFAULT now() NOT NULL,
                updated_at timestamp DEFAULT now() NOT NULL,
                deleted_at timestamp NULL
            )
            """
        )
    )
    
    conn.commit()
