import csv

def filter_csv(input_file, region_condition, specialization_condition, vendor_name):
    try:
        filtered_rows = []

        with open(input_file, 'r', encoding='utf-8-sig') as csv_file:
            reader = csv.DictReader(csv_file)
            if vendor_name:
                for row in reader:
                    if row['area'] == region_condition and row['specialty'] == specialization_condition and row["vendor_name"] == vendor_name:
                        filtered_rows.append(row)
            else:
                for row in reader:
                    if row['area'] == region_condition and row['specialty'] == specialization_condition:
                        filtered_rows.append(row)
                        
        print(f"Filtering completed. {len(filtered_rows)} rows matched the conditions.")
        return filtered_rows

    except Exception as e:
        print(f"Error processing the CSV file: {e}")
        return None
def process_data(filtered_data):
    try:
        if not filtered_data:
            return "لا توجد بيانات لهذا البحث، جرب تخصصًا آخر أو منطقة أخرى."

        result_text = ":بناءً على طلبك، قمت بفحص البيانات المقدمة وتصفيتها وفقًا للمعايير المحددة. إليك النتائج\n\n"

        for row in filtered_data:
            result_text += f"{row['vendor_name']}، متخصص في {row['specialty']}، يقع {row['address']} - {row['area']}.\n"
            
            if 'Price_after' in row:
                result_text += f"مميزات الشبكة: {row['Price_after']}\n"
            else:
                result_text += "يرجى الاتصال بالخط الساخن للحصول على التفاصيل.\n"

            result_text += f"للتواصل يمكنك الاتصال على الرقم {row.get('phone 2')}.\n\n"
        print(result_text)
        return result_text

    except Exception as e:
        print(f"Error processing the data: {e}")
        return "حدث خطأ أثناء معالجة البيانات."



