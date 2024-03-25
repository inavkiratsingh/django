from django.shortcuts import render
import oracledb

# Create your views here.


def register(request):
    if request.method == 'POST':
        conn = oracledb.connect(
            user='nav2', password='123', host="localhost", port=1521)
        cursor = conn.cursor()
        roll = request.POST['roll']
        name = request.POST['name']
        sex = request.POST['sex']
        marks = request.POST['marks']
        city = request.POST['city']
        c = cursor.execute('insert into student(roll, name, sex, marks, city) values(:roll,:name,:sex,:marks,:city)', [
                       roll, name, sex, marks, city])
        print(c)
        if c:
            print('success')
        conn.commit()

    return render(request , 'register.html')
