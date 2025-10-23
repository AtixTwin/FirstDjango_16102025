from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound

items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5, "img_url":"https://room78.net/wp-content/uploads/2022/06/gukb4qkvixirslxpsa6fcuk9u7qmvmsnpgj3yl1buo2mnrpttbvzatyzvgq5mv923kp-n16bpgtgiwa6enuhsi0k.jpg"},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2, "img_url":"https://img.joomcdn.net/02aaa28e02ea36a98dff0d50629eb6b7abb303a2_original.jpeg"},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12, "img_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQoB49TGPkGMQeN5BA4Fmv3NH9ZNVTnGJLsfg&s"},
   {"id": 7, "name": "Картофель фри" ,"quantity":0, "img_url":"https://marr.ru/upload/resize_cache/webp/iblock/21b/adaj3t6awf7l5bpts8j9tpaedis6wqkc.webp"},
   {"id": 8, "name": "Кепка" ,"quantity":124, "img_url":"https://vintageleder.ua/upload/products/img/large/kepka_huliganka_kozhanaya_muzhskaya_gatsby_art_23_vintage_leder.jpg"},
]

def main(request):
    context = {
        "name": "Алексеев Антон Юрьевич",
        "email": "atix.wind@gmail.com"
    }
    return render(request, "index.html", context)

def about(request):
    
    author = {
        "name": "Антон",
        "midle_name": "Юрьевич",
        "last_name": "Алексеев",
        "contact_number": "+7 (926) 655-52-20",
        "email": "atix.wind@gmail.com"
    }
    
    context = {
        "author": author,
    }

    return render(request, "about.html", context)

def item(request, id: int):

    if id > 5:
        
        url_not_found = "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxIQEhEREBEQEBUPFRAVEBATEBUQDxARFBIWFhcRExUYHSggGBolIBcVITEhJSkrLi4uGCAzODMsNygtLjcBCgoKDg0OGxAQGy8mICUtLTIrLy0vLy0tMDI1LjUtLS0tLS0tLS0tLy0tKy0rLS01LS0tLSstLSstLS0rLS0tK//AABEIALcBEwMBIgACEQEDEQH/xAAbAAEAAgMBAQAAAAAAAAAAAAAABAUBAwYCB//EAEgQAAEDAgIFBwcICAUFAAAAAAEAAgMEERIhBRMxQVEGFCJSYXGBMnKRkpShsRYkM0JUYsHiI1Nkk6Ky0dIVNHOCs0NjwuHw/8QAGQEBAAMBAQAAAAAAAAAAAAAAAAECAwQF/8QAKxEBAAICAQIEBgEFAAAAAAAAAAECAxEhEjEEE0FRIjJhcYHwFAUjM1KR/9oADAMBAAIRAxEAPwD7iiIgIiICIiAiIgIiICIiAiIgIiICIo7qm5sxuMjab2aPH+iibRHdMQkIozpJG5ua0gbQ0nEB2X2rex4IBGYOwqItE8Ew9IiKyBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREEeqJOFgNsd7neGjbb3DxWtztrWnVsjyc4bb8Bf4rZUXDmuALrBwIG3O2Y9CiNxBuJ7bWJIadr5XHK/YLrC88y0rHDbDP0JDcuDb4SRYno3sVnRzS3Ezq4T3XaCR6b+lY1XkR7bnHIeNjf3n4LbS5ukduLrD/aLfG6iu+qN/v7wTrUpKIi6GYiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAorulIBujGL/AHHIe66lKvc6zZ3b7kD1QB8VnklasMCQkFzfKmNmdjG5YvifFToow0Bo2BRqNmbj1bMb2AAfipijFHG5LT6CIi1VEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQFBqIX9MNAIkz22LXW29oyC2waQhkcWMlie4bWtka5w7wDdaatt3HE17hh6Abe2LO97bDszWWXWlq90iliLQcVruJJtsueC3rXACGtDsyALntWxXrGohE9xERWQIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiIC5rlDpeUS82p3tiLIxLUTlgldE1zi2OONhIBe8tfmcgGk2KvNI1zKeN0spwtba5ALiS4hoAaASSSQLDiuDrZ5ZZ6p8MTmtmkgLaioDoIsEdO1uEMI1jyHOlyDbdoUcb0mISaTlPUUrr1TudQE9KYRiOogHWexnRkZxLQCOBVxysqRJHTwsksysmYyR7HbadrHyyAOGzE1hbcddcx/hsZ+mknqTvbjNNTeEUZxEee4rRzGCGWkdFBBDadkZdGzC60zHwhpcSTa7271e1J7xHC81hKq6SKQYdVGwD6PVsbE+IbsD2AOaRxBVtya5QvY8UtY/GXA82qSADLhFzDIBlrQASD9YA7wVXhV/RqYsJfZxAddmT4Xh7tW9vBww3C1yUjXHdbUS+kMY93SLyy+xoDchuuSNq9ah361/oZ/RVnJLTBqof0lhNAdXUNGzGBk9v3XCzh39iu1yxSPVnMzCPqH/rXeq3+ixqZP1p8WNUlE6I/ZlHVKNqpP1o/dj+q884cxwbJY4tjgLZ3AsR4hS1W1RxPI4GNo7743e4BUyfDG4Wrz3WSIi2UEREBERAREQEREBERAREQEREBERAREQEREBYJWVz3LCoJbHStLmmrL9Y9ps6OmjbimcDuJGGMEbDIDuQU+mNJc+xNuRR3IAacMlc5pzdj2xwAjJzbOcRkQNtbVaxpL43PlG+CV+KQAboZjm7zX+tuUh7r7AGgABrBk1jQLNY0bgBksLpriiI+ryrePv17r29mqiq2TNxRm4vYgizmuG1r2nMOHBQq2pElM6aMEmL9K1p8oSU8mPCRxxR2UGtqHRVMsrAGxwxw85Fs5Gvc/9JwuwAG+0glWGi6cuilFnNEklVhOEjovkdZwB3HaO9Vm+/hn6vXw5Yy16oW1QRjcW7HHE3zXdJvuIVfoSnZHTRBgsXuqHyne6XXvYb9wY0DuU7k/T1E4cy9JAaRsMV3wST660TbSi8jA0Wyw2OYOa8ywupmMjqgI8GO9UAXUsz5JHPc8ltzCSXHovGEXADis4y1m0bXaYqw0k7KoeQ7DFVDcYi6zJT2scb+a5y+iNmB3r5w6pp5LxB4q3PBHN6Ya57wQQQ546EbfvOIUan5U1kFPGx0cUToQ9jZJ3GRtWYptVqmPYRZ4AJc43OVw0grHPkitt1kmu31AzALwajsXyGp5QVDZRLFPI9zSC7FI9tPNxjEF8Ece4WGLIEm67vk1ykjrg8BjopIsOsjcQ7J17Pa4ZObkRuItsXL/ACeqdQmcU1jl07ZAfDaoFEMTw4/eee95s33BYnfYWBzf0R45KRQNFnOGxxsPNb0R8Fet/MtEeyNdMSloiLqZCIiAiIgIiICIiAiIgIiICIiAuN0ryveZpYKVrLwuLHlzJKifGAPIpoRfDn5T3MGW8ZrslRVPJy8kkkFTU0pmdjlbE5hY9+ENx4ZGusbNGzgq236JhzksmkX9J76+IG9hi0fRtyBJIa4Su2AnN2wZrZTaUrqSambPziSGolbE6SfmzwzGDhc2anw2zsLOZY323sFO0jyOlmtj0lVOLBKGY44HNbrI3RuNgwXOFzht3qqqp5Z2upKmzYaRzYX6hxa+skjYx4cHnOFjQ5l7EuxZB1m5xFZmdFr1rG57PoSyuL0dpSSnPQ11RAfKhe8zVcFtr4nO6U7N5YemN2LYuq0fpCKoYJIZGyNOVwc2ne1w2tcN4OYV+Y4lSt62jdZ3CSuP0tUB81S/aI2w0zOx99dNbwMI8FfcoNJGnhLmND5ZCI6eM5CSd+TQSNjRm4nc1pO5ceGYGtjDi/BiLpDtlle4ukmPnOJPdZXx16rfZh4rLFMc+8tdPIJGaxmbQS1x6jxtY8fVd2FelV6UjeHfNC9lXK12qdG/AcLRcyTDMOjbl5QOZAG1WpnEoZIP+oyF+4eVE03y35ret92msvLviiMcZIUXKCne0TzMbjElO+OZlwHdFryyRt8jbEQRw7l9Xooxq47geQzd90L5xpk/N6j/AEpf5CvpNF9FH5jP5QsM1Y27/AWmaz+FdT2sC5rThOdwM2PNgfAqyFJH1G+qFXNFmNJ2Ws7ta7I+jb4Kwo33bY7WdF3bbYfEWK4cEx2l6d994ZNJH1G+hY5lH1G+hSEXT0V9me5RuYxfq2eqFnmUfUb6ApCKOivsdU+7RzSPqM9ULxC3A7APJcLtHAjaB6QfSpSjVmQa/qOB8DkfiotERzCYmZ4SURFoqIiICIiAiIgIiICIiAiIgIiICIiAuY5Qcmi9zqilIZMc5InEiCpsAOl1JLAAPHAAghdOiItWLRqXzOmqg8uYQ6OSO2theMMsROzEOHBwuDuKkFoLtZeSKXIc5hcI6iw2B9wWyjM5PBXW6e5PQ1gBeHMkjvqqiM4ZoyeB3j7puDwXIVejaylNpYjVRjZPTtvJb/uQbQfMuOwLWMkWjV3nW8NkxT1Yp/H73epqud0oM72T4WObDNG0xCNpPT1kRJtI4WGJpIs1w6NyotbVavC1rTJJISIYW+XI4C57mjaTuC9xiolyhpZxcgGSojdTRMubXIeA93cB4hdNo7QDKRr5HOM08jSJZ3CxIGxkbdjGDgPEk5ql81cdJii1PD5M94tl4hr5L6F5u0yykSTzhpmkA6IaMxDHfMRj3m5K52gbaJjdmqM8P7ioliH8LWru2DIDsC46ZtpKltrYKmT0Swwyj3ucufwlp8zn1dPjqR5Oo9NK3TxtTVJ4Qzf8ZX0yjFo2djG/yhfLuU7rUdV/oze9hC+qMFmgcGge5dWf5vw5/wCn/LP3QKcdBvcEp34HC+6zHeafId+C9wt6DDxaPgvEzd9r3BDgNpaeHaNq8yN11L1u6zRQIqwgWux9t+MNce9p2FbBW/cd4Fp/FdcZasuiUtFG54Oq/wBVOeDqv9QqfMp7nTKSvErMQIO8EelaeeDqyeoU52Oq/wBW3xUTkr7nTL3SPuxt9oyd3jIrcolA6+sNrAvJGd9wvmO1S1OOd1hFu4iIroEREBERAREQEREBERAREQEREBERAREQeXsDgQRcHaFBraRgYSL7gLucdrgOKsFF0h5IHFzPjf8ABZZYjpmZWpM7a1ymlWFtTVtP1mUMo7yJ4nfyRrr4GXN+C5flA8GrnHVpqQHvdPMR/K5R4aurRLLxXOK0fRzfKNt6aZvWaG+s9o/FfVHbD3FfMNLj9EfPg/5mL6e/Ye4rqz/N+HL4D/HP3aaRt42D7rfgtboyNy20jgI2E5ANbc+CxzxnE+q7+i5LVrMRudPQ53w0OYN4HiF41Teq31QpPPY+tbvBH4L1HURuyDmk8Li/oWflVntMJ3PsiahnVb6oWNQzqt9AVjgHAJqxwCn+Odau5uzqt9C20VMwsaSxpNs+iFM1Y4BaNH/RjsxD0OKmmKK25JtMw3taALAADgBYL0iLpZiIiAiIgIiICIiAiIgIiICIiAiIgIURBDNQ5r3XzaC0HLNoIFndovdS1EdhMj23BxMsR3f+nLGjZHEWcb2DSO4jYsa21bX3XmONpqi1ouYxxd8GkqUo0/0kX+8/w2/FXyRuukV7t7W2Flw3KKVsNVUGodqRUCl1ErwRDI2JkmKPGBZrgXuNnWuDlvXdLkp68nS7GSAauODVxG+yee8huPvMhIB+64b1bfTrSlqReJrLnXsbWFlPTSMmc98RkdE7WMgiZI1zpJHjojybBt7knZYEr6bL5Lu4rn9FTtOka+NpHQhoS4Dc46/I+GH0q/n8l3cfglrTbcyrixVxx01RZPoWDjqh6S1SJHPv0WtI4lxHustEn0LPu6onuBaSsvcxxvriOwPaB8FjvX/IbNl5erH6xP4LXVA4AXBtw5lrecFsZOxotrAe0vBK0VdQ19mtIccTSbZ2AN81F5rFZ5TG99k2N1xdel4iGQXtb17QzkUah8kjg6QfxEqSo1L5Ug4Ov6WgqtvmhMdpSVrmmDBc+A2kngAkkzWkAkAm9vBRmOyMzuBwDqt3AdpS1/SCISYZQ4XFxmQQciCNy2LTSR4WgHbtPnHMrcprvXJPcREVkCIiAiIgIiICIiAiIgi19ZqgDqppbm1omB5GW03IVeeUP7JXfuB/crpYLRvCrO/RKk+Uf7JX+zj+5Y+Uv7HX+zj+5XRibwC86gKv9z6J4c4/TvSLhR198TSPm27CAR5S2QcoQ0uPM6/Mi3zbYALD6yvzAO1Y5uOJWcUvE70ncKc8px9j0h7N+ZaPlH0y7mekPJAHzbZmSfrdyvub9vuWOb9vuUz5k+hwqPlOPsekPZvzLl+UtRJNM2aCjrgTGA8mnwkSwP11NIDizAdjYR1ZTwXf837U5ueIUTOSfQjTitKaSk1kdVS0ldHM2wniNI0sqYy5uJj3YsnNsS13hsKu5uUoLXAUekMwQPmp3jvVzzc8QnNzxCbyexwpouUwDQOZ6QyAH+V4Dzlpfp5hN+ZV/sl//JX/ADc8QnNzxCiYvMamDcOf/wAcb9ir/Y/zLI5QD7HpD2X8yv8Am54hObniFTon/VPV9VOOVA+xaR9m/Mnyq/YtI+zfmVxzc8Qs83PELXeT2R8Kl+VX7FpH2b8y0u5SdMOFFpEbn/Ntotl9baug5v2+5Z5v2+5RPmT6EahzlVp/Gf8AJ6QsWuB+bcSCD5XYvVTyiLgGij0iACCSKYXy2AdL/wCsuhFP2rPNxxKiaXnfHdO4UUHKc2GKj0hewuebDb4OW0cph9j0h7N+ZXOoHb6VkQt4LSPMV4Uw5Sj7JX+z/mUmj01rHBvNqtmL60kIawd5urIRjgPQvStEW9UcCIiugREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREH/9k="  
        
        text = f"""
        <!doctype html>
        <html lang="ru">
        <meta charset="utf-8">
        <title>Товар не найден</title>
        <h1>Tовар с ID #{id} не найден</h1>
        <style>
            .img-fixed {{
                width: 360px;       
                height: 360px;      
                object-fit: cover;  
                object-position: center; 
                border-radius: 10px; 
            }}
            </style>
        <img class="img-fixed" src="{url_not_found}" alt="NOT FOUND">
        <br>
        <br>
        <a href="http://127.0.0.1:8000/items/">Назад к списку товаров</a>
        """
        return HttpResponseNotFound(text)
    
    else:

        SKU = {
            "SKU_ID": items[id-1]["id"],
            "SKU_name": items[id-1]['name'],
            "SKU_img": items[id-1]['img_url'],
            "SKU_quantity": items[id-1]['quantity'],
        }
        
        context = {
            "SKU": SKU
        }

        return render(request, "item_page.html", context)
    

def items_def(request):

    context = {
        "SKU_List": items
    }    

    return render(request, "items_list.html", context)
