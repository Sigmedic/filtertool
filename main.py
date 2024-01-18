from flask import Flask, render_template, request
from filter import filter_csv, process_data  # Make sure this import is correct
import random

app = Flask(__name__)

# Define your areas and specialties here
areas = ['وسط البلد', 'العباسية', 'السيدة زينب', 'العباسيه', 'حدائق القبة', 'مصر الجديدة', 'مدينة نصر', 'سيتى ستار ', 'عباس', 'روكسي ', 'مدينة نصر ', 'مصر القديمه', 'مصر القديمة', 'المعادي', 'زهراء المعادى', 'حلوان', ' حلوان', 'المقطم', 'الجمعة الحديثة', 'المقطم ', 'الزيتون', 'عين شمس', 'جسر السويس', 'المطرية', 'مدينة السلام', 'الخصوص', 'العبور', 'العبور ', ' العبور', 'الشروق', 'الشروق ', 'التجمع الخامس', 'التجمع الاول', 'القطامية ', 'التجمع الأول', 'التجمع الثالث', 'الرحاب ', 'الرحاب', 'مدينتي',  'مدينة بدر', 'بدر 2', 'بدر1', 'شبرا ', 'شبرا', 'شبرا مصر', 'شبرا الخيمة', 'المنيل', 'القصر العينى', 'الزمالك', 'المهندسين', 'الهرم']
specialties = ['جميع التخصصات', 'أطفال', 'كلي ', 'رمد', 'مسالك بولية', 'قلب', 'أدوية', 'أشعة وتحاليل', 'تحاليل', 'تحاليل واشعه', 'أشعة', 'اشعه ', 'اسنان', 'باطنى', 'جراحة', 'تجميل', 'صدر', 'مخ وأعصاب', 'عظام', 'جراحة قلب وصدر ', 'علاج طبيعي', 'نظارات طبية', 'ادوية', 'اشعه', 'نساء وتوليد', 'انف واذن', 'أورام', 'أشعة أسنان ', 'جراحه عظام', 'جرراحه عامه وجراحه اورام', 'جلدية', 'مخ واعصاب', 'جراحه عامه', 'قلب وصدر', 'قلب وقسطرة', 'علاج طبيعي ', 'الرعايه الصحية', 'هضمى وكبد', 'هضمى', 'جلدية ', 'علاج طبيعى', 'قلب واوعيه دمويه', 'رمد ','مناظير جهاز هضمى', 'جراحة مسالك بولية']
text_random = [
    ':بناءً على طلبك، قمت بفحص البيانات المقدمة وتصفيتها وفقًا للمعايير المحددة. إليك النتائج',
    'وفقًا لطلبك، تم تحليل البيانات المقدمة ومعالجتها بناءً على المعايير التي حددتها. ها هي النتائج',
    'استجابةً لطلبك، تمت مراجعة البيانات المُعطاة وتنقيتها طبقًا للمعايير الموضوعة. تفضل بمشاهدة النتائج'
]


app = Flask(__name__)

# Inside filter.py

def process_data(filtered_data):
    # Assuming 'filtered_data' is a list of dictionaries
    # Modify this function to generate a single HTML string with all results
    if not filtered_data:
        return "No results found."    
    results_html = '<div class="results-container">'
    results_html += f'<div class="result-item"><p>{text_random[random.randint(1,3)]}</p></div>'
    for row in filtered_data:
        results_html += f'<div class="result-item"><p>{row['vendor_name']}، متخصص في {row['specialty']}، يقع {row['address']} - {row['area']}.</p></div>'
        if 'Price_after' in row:
                results_html += f'<div class="result-item"><p>مميزات الشبكة: {row['Price_after']}.</p></div>'
        else:
                results_html += f'<div class="result-item"><p>يرجى الاتصال بالخط الساخن للحصول على التفاصيل.</p></div>'
    results_html += '</div>'
    return results_html


@app.route('/search', methods=['GET'])
def search():
    # Get values from the form
    area = request.args.get('area')
    specialty = request.args.get('speciality')
    name = request.args.get('name')  # Assuming you want to use 'name' for additional filtering

    # Path to your CSV file
    csv_file_path = 'data.csv'  # Update this with the actual path to your CSV file

    # Call filter_csv from filter.py
    filtered_data = filter_csv(csv_file_path, area, specialty,name)

    # Call process_data and get a single HTML string with all results
    results_html = process_data(filtered_data)

    # Pass the HTML string to the template
    return render_template('index.html', areas=areas, specialties=specialties, results=results_html)


@app.route('/')
def index():
    return render_template('index.html', areas=areas, specialties=specialties)

if __name__ == '__main__':
    app.run(debug=True)
