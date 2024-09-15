from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm
from django.templatetags.static import static

def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()  # Save data to MySQL
            return redirect('success_page')  # Redirect after successful save
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
def toppick(request, id):
    # Sample movie data with more details
    movies = {
        1: {
            'title': 'Green Book',
            'description': ' หนังสือสีเขียว หรือ Green Book ที่เป็นชื่อหนัง ก็คือหนังสือ The Negro Motorist Green Book หนังสือไกด์บุคที่เขียนโดย วิกเตอร์ ฮูโก กรีน สำหรับนักท่องเที่ยวหรือจะเรียกให้หรูหน่อยก็คือนักเดินทางผิวดำ ในการหาที่พัก, ร้านอาหาร หรือสถานที่ต่างๆ ที่ต้อนรับพวกเขา ซึ่งตีพิมพ์ออกมาในช่วงกลางยุค 20 ยุคที่ปัญหาเรื่องสีผิวยังไม่ถูกเก็บซ่อน หรือถูกทำให้พร่าเลือน',
            'director': 'Peter Farrelly',
            'release_date': '2018-11-16',
            'genre': 'Drama, Comedy',
            'poster': 'POSTER1.png',
            'video': 'green.mp4',
            'img' : 'greenbookactor.jpg',
            'actor_image': 'greenbookactor.jpg',
            'actors': [
                {'name': 'Viggo Mortensen', 'image': 'Viggo.jpeg'},
                {'name': 'Mahershala Ali', 'image': 'mahershala.jpg'},
                {'name': 'Linda Cardellini', 'image': 'linda.jpg'},
                {'name': 'Sebastian Maniscalco', 'image': 'linda.jpg'},
                {'name': 'Dimiter D. Marinov', 'image': 'linda.jpg'},
                {'name': 'Joe Cortese', 'image': 'linda.jpg'},
                {'name': 'Irene Sirko', 'image': 'linda.jpg'},
                {'name': 'P.J. Byrne', 'image': 'linda.jpg'},
                {'name': 'Michael McKinney', 'image': 'linda.jpg'},
                {'name': 'Misty Copeland', 'image': 'linda.jpg'},
            ]
        },
        2: {
            'title': 'Black Panther',
            'description': 'TChalla, heir to the hidden but advanced kingdom of Wakanda, must step forward to lead his people into a new future and must confront a challenger from his countrys past.',
            'director': 'Ryan Coogler',
            'release_date': '2018-02-16',
            'genre': 'Action, Adventure',
            'poster': 'POSTER2.png',  # Fallback image if video is unavailable
            'video': 'blackpanter.mp4',  # Background video for Black Panther
            'actor_image': 'blackpantheractor.jpg',  # Fallback actor image
            'actors': [
                {'name': 'Chadwick Boseman', 'image': 'Viggo.jpeg'},
                {'name': 'Michael B. Jordan', 'image': 'mahershala.jpg'},
                {'name': 'Lupita Nyong', 'image': 'linda.jpg'},
                {'name': 'Danai Gurira', 'image': 'linda.jpg'},
                {'name': 'Martin Freeman', 'image': 'linda.jpg'},
                {'name': 'Daniel Kaluuya', 'image': 'linda.jpg'},
                {'name': 'Letitia Wright', 'image': 'linda.jpg'},
                {'name': 'Winston Duke', 'image': 'linda.jpg'},
                {'name': 'Sterling K. Brown', 'image': 'linda.jpg'},
                {'name': 'Angela Bassett', 'image': 'linda.jpg'},
            ]
        },
        3: {
            'title': 'Moonfall',
            'description': 'เมื่อดวงจันทร์หลุดออกจากวงโคจรและกำลังพุ่งชนโลก มนุษยชาติต้องหาทางหยุดยั้งหายนะนี้',
            'director': 'Roland Emmerich',
            'release_date': '2022-02-04',
            'genre': 'Science Fiction, Action',
            'poster': 'POSTER3.png',
            'video': 'moonfall.mp4',
            'actor_image': 'moonfallactor.jpg',
            'actors': [
                {'name': 'Halle Berry', 'image': 'halle.jpg'},
                {'name': 'Patrick Wilson', 'image': 'patrick.jpg'},
                {'name': 'John Bradley', 'image': 'john.jpg'},
                {'name': 'Donald Sutherland', 'image': 'john.jpg'},
                {'name': 'Michael Peña', 'image': 'john.jpg'},
                {'name': 'Charlie Plummer', 'image': 'john.jpg'},
                {'name': 'Kelly Yu', 'image': 'john.jpg'},
                {'name': 'Max Mauff', 'image': 'john.jpg'},
                {'name': 'Elyes Gabel', 'image': 'john.jpg'},
                {'name': 'Catherine Keener', 'image': 'john.jpg'},
            ]
        },
        4: {
            'title': 'Titanic',
            'description': 'เรื่องราวโศกนาฏกรรมของเรือไททานิกที่จมลงในมหาสมุทรแอตแลนติก หลังชนภูเขาน้ำแข็ง',
            'director': 'James Cameron',
            'release_date': '1997-12-19',
            'genre': 'Drama, Romance',
            'poster': 'POSTER4.png',
            'video': 'titanic.mp4',
            'actor_image': 'titanicactor.jpg',
            'actors': [
                {'name': 'Leonardo DiCaprio', 'image': 'leo.jpg'},
                {'name': 'Kate Winslet', 'image': 'kate.jpg'},
                {'name': 'Billy Zane', 'image': 'billy.jpg'},
                {'name': 'Kathy Bates', 'image': ''},
                {'name': 'Frances Fisher', 'image': ''},
                {'name': 'Gloria Stuart', 'image': ''},
                {'name': 'Bill Paxton', 'image': ''},
                {'name': 'Bernard Hill', 'image': ''},
                {'name': 'David Warner', 'image': ''},
                {'name': 'Victor Garber', 'image': ''},
            ]
        },
        5: {
            'title': 'Friday the 13th',
            'description': 'เรื่องราวของกลุ่มวัยรุ่นที่ถูกล่าโดยฆาตกรสวมหน้ากากในวันศุกร์ที่ 13',
            'director': 'Sean S. Cunningham',
            'release_date': '1980-05-09',
            'genre': 'Horror, Thriller',
            'poster': 'POSTER5.png',
            'video': '13friday.mp4',
            'actor_image': 'fridayactor.jpg',
            'actors': [
                {'name': 'Betsy Palmer', 'image': 'betsy.jpg'},
                {'name': 'Adrienne King', 'image': 'adrienne.jpg'},
                {'name': 'Jeannine Taylor', 'image': 'harry.jpg'},
                {'name': 'Robbi Morgan', 'image': 'harry.jpg'},
                {'name': 'Kevin Bacon', 'image': 'harry.jpg'},
                {'name': 'Harry Crosby', 'image': 'harry.jpg'},
                {'name': 'Laurie Bartram', 'image': 'harry.jpg'},
                {'name': 'Mark Nelson', 'image': 'harry.jpg'},
                {'name': 'Renee Jones ', 'image': 'harry.jpg'},
                {'name': 'Peter Browning', 'image': 'harry.jpg'},
            ]
        },
        6: {
            'title': '9Sadtra',
            'description': 'หนังแนวไซไฟที่เล่าเรื่องการสำรวจอวกาศที่ห่างไกล',
            'director': 'Jane Doe',
            'release_date': '2023-08-15',
            'genre': 'Science Fiction, Drama',
            'poster': 'POSTER6.png',
            'video': '99.mp4',
            'actor_image': 'sadtraactor.jpg',
            'actors': [
                {'name': 'Actor P', 'image': 'actorP.jpg'},
                {'name': 'Actor Q', 'image': 'actorQ.jpg'},
                {'name': 'Actor R', 'image': 'actorR.jpg'},
            ]
        },
    }

    # Get the selected movie by ID, with a default fallback
    movie = movies.get(id, {
        'title': 'Unknown Movie',
        'description': 'No description available',
        'poster': 'default.png',
        'actor_image': 'defaultactor.jpg',
        'actors': []
    })

    # Here you would typically render a template with the movie data
    # Example: return render(request, 'movie_detail.html', {'movie': movie})
    return render(request, 'toppick.html', {'movie': movie})



def coming_soon_detail(request, id):
    # ดึงข้อมูลหนังที่กำลังจะมาในอนาคต
    movie = {'id': id, 'title': f'Coming Soon {id}', 'description': 'ตัวอย่างหนัง'}
    return render(request, 'coming_soon_detail.html', {'movie': movie})

def celebrity_detail(request, id):
    # ดึงข้อมูลดารา
    celebrity = {'id': id, 'name': f'Celebrity {id}', 'bio': 'ข้อมูลของดารา'}
    return render(request, 'celebrity_detail.html', {'celebrity': celebrity})

def news_detail(request, id):
    # ดึงข้อมูลข่าว
    news = {'id': id, 'title': f'News {id}', 'content': 'เนื้อหาข่าว'}
    return render(request, 'news_detail.html', {'news': news})

