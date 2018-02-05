{"filter":false,"title":"models.py","tooltip":"/mypage/models.py","undoManager":{"mark":94,"position":94,"stack":[[{"start":{"row":5,"column":0},"end":{"row":17,"column":52},"action":"remove","lines":["class Post(models.Model):","    author = models.CharField(max_length=10)","    title = models.CharField(max_length=50)","    content = models.TextField()","    created_at = models.DateTimeField(auto_now_add=True)","    updated_at = models.DateTimeField(auto_now=True)","","class Comment(models.Model):","    post = models.ForeignKey(Post)","    author = models.CharField(max_length=10)","    message = models.TextField()","    created_at = models.DateTimeField(auto_now_add=True)","    updated_at = models.DateTimeField(auto_now=True)"],"id":5},{"start":{"row":5,"column":0},"end":{"row":17,"column":52},"action":"insert","lines":["class Post(models.Model):","    author = models.CharField(max_length=10)","    title = models.CharField(max_length=50)","    content = models.TextField()","    created_at = models.DateTimeField(auto_now_add=True)","    updated_at = models.DateTimeField(auto_now=True)","","class Comment(models.Model):","    post = models.ForeignKey(Post)","    author = models.CharField(max_length=10)","    message = models.TextField()","    created_at = models.DateTimeField(auto_now_add=True)","    updated_at = models.DateTimeField(auto_now=True)"]}],[{"start":{"row":10,"column":52},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":6},{"start":{"row":11,"column":0},"end":{"row":11,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":11,"column":4},"end":{"row":13,"column":0},"action":"insert","lines":["def __str__(self):","        return self.title",""],"id":7}],[{"start":{"row":20,"column":52},"end":{"row":21,"column":0},"action":"insert","lines":["",""],"id":8},{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":21,"column":4},"end":{"row":22,"column":27},"action":"insert","lines":["def __str__(self):","        return self.message"],"id":9}],[{"start":{"row":22,"column":27},"end":{"row":23,"column":0},"action":"insert","lines":["",""],"id":10},{"start":{"row":23,"column":0},"end":{"row":23,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":23,"column":8},"end":{"row":24,"column":0},"action":"insert","lines":["",""],"id":11},{"start":{"row":24,"column":0},"end":{"row":24,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":24,"column":4},"end":{"row":24,"column":8},"action":"remove","lines":["    "],"id":12}],[{"start":{"row":24,"column":0},"end":{"row":24,"column":4},"action":"remove","lines":["    "],"id":13}],[{"start":{"row":24,"column":0},"end":{"row":25,"column":52},"action":"insert","lines":["class PostAdmin(admin.ModelAdmin):","    list_display = ['author', 'title', 'created_at']"],"id":14}],[{"start":{"row":25,"column":52},"end":{"row":26,"column":0},"action":"insert","lines":["",""],"id":15},{"start":{"row":26,"column":0},"end":{"row":26,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":26,"column":4},"end":{"row":26,"column":35},"action":"insert","lines":[" list_display_links = ['title']"],"id":16}],[{"start":{"row":26,"column":4},"end":{"row":26,"column":5},"action":"remove","lines":[" "],"id":17}],[{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["from django.contrib import admin",""],"id":18}],[{"start":{"row":27,"column":34},"end":{"row":28,"column":0},"action":"insert","lines":["",""],"id":19},{"start":{"row":28,"column":0},"end":{"row":28,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":28,"column":4},"end":{"row":29,"column":0},"action":"insert","lines":["",""],"id":20},{"start":{"row":29,"column":0},"end":{"row":29,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":29,"column":0},"end":{"row":29,"column":4},"action":"remove","lines":["    "],"id":21}],[{"start":{"row":29,"column":0},"end":{"row":29,"column":1},"action":"insert","lines":["c"],"id":22}],[{"start":{"row":29,"column":1},"end":{"row":29,"column":2},"action":"insert","lines":["l"],"id":23}],[{"start":{"row":29,"column":2},"end":{"row":29,"column":3},"action":"insert","lines":["a"],"id":24}],[{"start":{"row":29,"column":3},"end":{"row":29,"column":4},"action":"insert","lines":["s"],"id":25}],[{"start":{"row":29,"column":4},"end":{"row":29,"column":5},"action":"insert","lines":["s"],"id":26}],[{"start":{"row":29,"column":5},"end":{"row":29,"column":6},"action":"insert","lines":[" "],"id":27}],[{"start":{"row":29,"column":6},"end":{"row":29,"column":7},"action":"insert","lines":["C"],"id":28}],[{"start":{"row":29,"column":7},"end":{"row":29,"column":8},"action":"insert","lines":["o"],"id":29}],[{"start":{"row":29,"column":8},"end":{"row":29,"column":9},"action":"insert","lines":["m"],"id":30}],[{"start":{"row":29,"column":9},"end":{"row":29,"column":10},"action":"insert","lines":["m"],"id":31}],[{"start":{"row":29,"column":10},"end":{"row":29,"column":11},"action":"insert","lines":["e"],"id":32}],[{"start":{"row":29,"column":11},"end":{"row":29,"column":12},"action":"insert","lines":["n"],"id":33}],[{"start":{"row":29,"column":12},"end":{"row":29,"column":13},"action":"insert","lines":["t"],"id":34}],[{"start":{"row":29,"column":13},"end":{"row":29,"column":14},"action":"insert","lines":["A"],"id":35}],[{"start":{"row":29,"column":14},"end":{"row":29,"column":15},"action":"insert","lines":["d"],"id":36}],[{"start":{"row":29,"column":15},"end":{"row":29,"column":16},"action":"insert","lines":["m"],"id":37}],[{"start":{"row":29,"column":16},"end":{"row":29,"column":17},"action":"insert","lines":["i"],"id":38}],[{"start":{"row":29,"column":17},"end":{"row":29,"column":18},"action":"insert","lines":["n"],"id":39}],[{"start":{"row":29,"column":18},"end":{"row":29,"column":20},"action":"insert","lines":["()"],"id":40}],[{"start":{"row":29,"column":19},"end":{"row":29,"column":20},"action":"insert","lines":["a"],"id":41}],[{"start":{"row":29,"column":20},"end":{"row":29,"column":21},"action":"insert","lines":["d"],"id":42}],[{"start":{"row":29,"column":21},"end":{"row":29,"column":22},"action":"insert","lines":["m"],"id":43}],[{"start":{"row":29,"column":22},"end":{"row":29,"column":23},"action":"insert","lines":["i"],"id":44}],[{"start":{"row":29,"column":23},"end":{"row":29,"column":24},"action":"insert","lines":["n"],"id":45}],[{"start":{"row":29,"column":24},"end":{"row":29,"column":25},"action":"insert","lines":["."],"id":46}],[{"start":{"row":29,"column":25},"end":{"row":29,"column":26},"action":"insert","lines":["M"],"id":47}],[{"start":{"row":29,"column":26},"end":{"row":29,"column":27},"action":"insert","lines":["o"],"id":48}],[{"start":{"row":29,"column":27},"end":{"row":29,"column":28},"action":"insert","lines":["d"],"id":49}],[{"start":{"row":29,"column":28},"end":{"row":29,"column":29},"action":"insert","lines":["e"],"id":50}],[{"start":{"row":29,"column":29},"end":{"row":29,"column":30},"action":"insert","lines":["l"],"id":51}],[{"start":{"row":29,"column":30},"end":{"row":29,"column":31},"action":"insert","lines":["A"],"id":52}],[{"start":{"row":29,"column":31},"end":{"row":29,"column":32},"action":"insert","lines":["d"],"id":53}],[{"start":{"row":29,"column":32},"end":{"row":29,"column":33},"action":"insert","lines":["m"],"id":54}],[{"start":{"row":29,"column":33},"end":{"row":29,"column":34},"action":"insert","lines":["i"],"id":55}],[{"start":{"row":29,"column":34},"end":{"row":29,"column":35},"action":"insert","lines":["n"],"id":56}],[{"start":{"row":29,"column":36},"end":{"row":29,"column":37},"action":"insert","lines":[":"],"id":57}],[{"start":{"row":29,"column":37},"end":{"row":30,"column":0},"action":"insert","lines":["",""],"id":58},{"start":{"row":30,"column":0},"end":{"row":30,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":30,"column":4},"end":{"row":31,"column":34},"action":"insert","lines":["list_display = ['author', 'title', 'created_at']","    list_display_links = ['title']"],"id":59}],[{"start":{"row":30,"column":35},"end":{"row":30,"column":36},"action":"remove","lines":["e"],"id":60}],[{"start":{"row":30,"column":34},"end":{"row":30,"column":35},"action":"remove","lines":["l"],"id":61}],[{"start":{"row":30,"column":33},"end":{"row":30,"column":34},"action":"remove","lines":["t"],"id":62}],[{"start":{"row":30,"column":32},"end":{"row":30,"column":33},"action":"remove","lines":["i"],"id":63}],[{"start":{"row":30,"column":31},"end":{"row":30,"column":32},"action":"remove","lines":["t"],"id":64}],[{"start":{"row":30,"column":31},"end":{"row":30,"column":32},"action":"insert","lines":["m"],"id":65}],[{"start":{"row":30,"column":32},"end":{"row":30,"column":33},"action":"insert","lines":["e"],"id":66}],[{"start":{"row":30,"column":33},"end":{"row":30,"column":34},"action":"insert","lines":["s"],"id":67}],[{"start":{"row":30,"column":34},"end":{"row":30,"column":35},"action":"insert","lines":["s"],"id":68}],[{"start":{"row":30,"column":35},"end":{"row":30,"column":36},"action":"insert","lines":["a"],"id":69}],[{"start":{"row":30,"column":36},"end":{"row":30,"column":37},"action":"insert","lines":["g"],"id":70}],[{"start":{"row":30,"column":37},"end":{"row":30,"column":38},"action":"insert","lines":["e"],"id":71}],[{"start":{"row":31,"column":31},"end":{"row":31,"column":32},"action":"remove","lines":["e"],"id":72}],[{"start":{"row":31,"column":30},"end":{"row":31,"column":31},"action":"remove","lines":["l"],"id":73}],[{"start":{"row":31,"column":29},"end":{"row":31,"column":30},"action":"remove","lines":["t"],"id":74}],[{"start":{"row":31,"column":28},"end":{"row":31,"column":29},"action":"remove","lines":["i"],"id":75}],[{"start":{"row":31,"column":27},"end":{"row":31,"column":28},"action":"remove","lines":["t"],"id":76}],[{"start":{"row":31,"column":27},"end":{"row":31,"column":28},"action":"insert","lines":["m"],"id":77}],[{"start":{"row":31,"column":28},"end":{"row":31,"column":29},"action":"insert","lines":["e"],"id":78}],[{"start":{"row":31,"column":29},"end":{"row":31,"column":30},"action":"insert","lines":["s"],"id":79}],[{"start":{"row":31,"column":30},"end":{"row":31,"column":31},"action":"insert","lines":["s"],"id":80}],[{"start":{"row":31,"column":31},"end":{"row":31,"column":32},"action":"insert","lines":["a"],"id":81}],[{"start":{"row":31,"column":32},"end":{"row":31,"column":33},"action":"insert","lines":["g"],"id":82}],[{"start":{"row":31,"column":33},"end":{"row":31,"column":34},"action":"insert","lines":["e"],"id":83}],[{"start":{"row":19,"column":10},"end":{"row":19,"column":11},"action":"remove","lines":["e"],"id":84}],[{"start":{"row":19,"column":9},"end":{"row":19,"column":10},"action":"remove","lines":["g"],"id":85}],[{"start":{"row":19,"column":8},"end":{"row":19,"column":9},"action":"remove","lines":["a"],"id":86}],[{"start":{"row":19,"column":7},"end":{"row":19,"column":8},"action":"remove","lines":["s"],"id":87}],[{"start":{"row":19,"column":6},"end":{"row":19,"column":7},"action":"remove","lines":["s"],"id":88}],[{"start":{"row":19,"column":5},"end":{"row":19,"column":6},"action":"remove","lines":["e"],"id":89}],[{"start":{"row":19,"column":4},"end":{"row":19,"column":5},"action":"remove","lines":["m"],"id":90}],[{"start":{"row":19,"column":4},"end":{"row":19,"column":5},"action":"insert","lines":["ㅅ"],"id":91}],[{"start":{"row":19,"column":4},"end":{"row":19,"column":5},"action":"remove","lines":["ㅅ"],"id":93}],[{"start":{"row":19,"column":4},"end":{"row":19,"column":5},"action":"insert","lines":["m"],"id":94}],[{"start":{"row":19,"column":5},"end":{"row":19,"column":6},"action":"insert","lines":["e"],"id":95}],[{"start":{"row":19,"column":6},"end":{"row":19,"column":7},"action":"insert","lines":["s"],"id":96}],[{"start":{"row":19,"column":7},"end":{"row":19,"column":8},"action":"insert","lines":["s"],"id":97}],[{"start":{"row":19,"column":8},"end":{"row":19,"column":9},"action":"insert","lines":["a"],"id":98}],[{"start":{"row":19,"column":9},"end":{"row":19,"column":10},"action":"insert","lines":["g"],"id":99}],[{"start":{"row":19,"column":10},"end":{"row":19,"column":11},"action":"insert","lines":["e"],"id":100}]]},"ace":{"folds":[],"scrolltop":60,"scrollleft":0,"selection":{"start":{"row":19,"column":4},"end":{"row":19,"column":4},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":20,"state":"start","mode":"ace/mode/python"}},"timestamp":1517756268129,"hash":"f6b85f6b1e68e48585c86410f9ba40dffce8ea7d"}