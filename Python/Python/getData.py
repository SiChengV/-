import getUrl
import requests
import get_request
from bs4 import BeautifulSoup

class Html_Data:
    # 返回一个列表和一个本页面的url
    def get_html(self, url):
        pa = get_request.GetRequests()
        #dic={}
        r = pa.run_url(url)
        print(r.status_code)
        html = BeautifulSoup(r.text, "html.parser")
        movieName = html.find("div", id="content").find('h1').find("span").get_text()
        director = html.find("div", id="info").find("span", class_="attrs").get_text()
        str = html.find_all("span", property="v:genre")
        kind = ""
        for i in str:
            kind = kind + i.get_text()
        #dic.update({"电影":"{}".format(movieName), "导演":"{}".format(director),"类型":"{}".format(kind)})
        # 爬取时长
        time = html.find("span", property="v:runtime").get_text()
        #dic.update({"时长":"{}".format(time)})
        # 发布日期
        releaseDate = html.find("div", id="info").find("span", property="v:initialReleaseDate").get_text()
        releaseDate = releaseDate[0:10]
        #dic.update({"发布日期":"{}".format(releaseDate)})
        # 评分
        score = html.find("strong", class_="ll rating_num").get_text()
        #dic.update({"评分":"{}".format(score)})
        # 总评数
        sumComment = html.find("span", property="v:votes").get_text()
        #dic.update({"总评数":"{}".format(sumComment)})
        #dic.update({"电影":"{}".format(movieName), "时长":"{}".format(time), "导演":"{}".format(director), "类型":"{}".format(kind), "发布日期":"{}".format(releaseDate), "评分":"{}".format(score), "总评数":"{}".format(sumComment)})
        list = [movieName,time,director,kind,releaseDate,score,sumComment]
        print(list)
        return list, r.url, movieName

    # 获取评论信息
    def get_comment(self, url):
        pa = get_request.GetRequests()
        list = []
        r = pa.run_url(url+"comments?status=P")
        print(r.status_code)

        html = BeautifulSoup(r.text, "html.parser")
        commentList = html.find("div", id="comments").find_all("div", class_="comment-item")
        i = 1
        # dic_2 = {}
        lists = []
        for user_comment in commentList:
            dic = {}
            userName = user_comment.find("span", class_="comment-info").find("a").get_text()
            # dic["用户"]="{}".format(userName)
            try:
                score = user_comment.find("span", class_="allstar50 rating")["title"]
                # dic["分数等级"]="{}".format(score)
            except:
                # dic["分数等级"]="空"
                score = '空'
            comment = user_comment.find("span", class_="short").get_text()
            time = user_comment.find("span", class_="comment-time").get_text().strip()
            # dic["评论"]="{}".format(comment)
            # dic_2[i] = dic
            # i += 1
            lis = [userName, score, time, comment]
            lists.append(lis)
        return lists

       
    def get_movie_score(self, url):
        pa = get_request.GetRequests()
        dic={}
        r = pa.run_url(url)
        print(r.status_code)
        html = BeautifulSoup(r.text, "html.parser")
        scoreList = html.find("div", class_="ratings-on-weight").find_all("div", class_="item")
        movieName = html.find("div", id="content").find('h1').find("span").get_text()
        i = 5
        for score in scoreList:
            rate = score.find("span", class_="rating_per").get_text()
            rate = rate.replace('%','')
            
            dic["{}星".format(i)]="{}".format(rate)
            i = i-1

        print(dic)
        list = []
        list.append(movieName)
        list.append(dic['5星'])
        list.append(dic['4星'])
        list.append(dic['3星'])
        list.append(dic['2星'])
        list.append(dic['1星'])
        print(list)
        return list


    def get_movie_play(self, url):
        pa = get_request.GetRequests()
        dic={}
        r = pa.run_url(url)
        print(r.status_code)
        html = BeautifulSoup(r.text, "html.parser")
        playList = html.find("ul", class_="bs").find_all("li")
        movieName = html.find("div", id="content").find('h1').find("span").get_text()
        lists = []
        for play in playList:
            web = play.find('a')['data-cn']
            url = play.find('a')['href']
            tup = (movieName, web, url)
            lists.append(list(tup))
            # dic['{}'.format(web)]="{}".format(url)
        print('播放链接：' , lists)
        return lists

    def get_movie_awards(self, url):
        pa = get_request.GetRequests()
        dic={}
        r = pa.run_url(url)
        print(r.status_code)
        html = BeautifulSoup(r.text, "html.parser")
        awardsList = html.find("div", class_="mod").find_all("ul")
        for award in awardsList:
            award_name = award.find("li").get_text().replace('\n','').replace('\t','').replace(' ','')
            award_info = award.find("li").find_next("li").get_text().replace('\n','').replace('\t','').replace(' ','')
            dic['{}'.format(award_name)]="{}".format(award_info)
        print(dic)
        return dic
