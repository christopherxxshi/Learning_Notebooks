# CSS 基础 - 布局无关属性

## 基本规则

```CSS
选择器{
    属性:值;
    属性:值;
}
```

- 选择器
    - 用于匹配HTML元素
    - 有不同的匹配规则
    - 多个选择器可以叠加
    
## 分类和权重

### 分类
    
- 元素选择器 `a{}`
- 伪元素选择器 `::before{}`
- 类选择器 `.link{}`
- 属性选择器 `[type = radio]{}`
- 伪类选择器 `:hover{}`
- ID选择器 `#id{}`
- 组合选择器 `[type=checkbox]+label{}`
- 否定选择器 `:not(.link){}`
- 通用选择器 `*{}`

### 权重（从高到低）

 1. ID选择器 `#id{}` +100
 2. 类 属性 伪类 +10
 3. 元素 伪元素 +1
 4. 其他选择器 +0
 
 - 权重计算结果不进位
 - `！important`优先级最高
 - 元素属性，优先级高
 - 相同权重，后写的生效



## 解析方式和性能

- 解析方式：从右往左解析，解析的过程进行验证。
    
    
## 值得关注的选择器

## 非布局样式

###分类

- 字体、字重、颜色、大小、行高
- 背景、边框
- 滚动、换行
- 粗体、斜体、下划线
- 其他

### 字体

- 字体族 font-family
    - 衬线 serif 
    - 非衬线 sans-serif 
    - 等宽 monospace 
    - 手写体 cursive 
    - 花体 fantasy
- 多字体 fallback（针对每一个字符）
- 网络字体、自定义字体

    ```CSS
    @font-face{
        font-family:"名称",
        src: url("路径 or 远程地址（跨域？ cois）")
    }
    ```
    
- iconfont

**注意：**

- 字体名称要加引号， 字体族不可以加引号

### 行高

- line-box 由最高的 inline-box 行高(line-hight)决定 
- inline-box（设置了line-height）在line-box中垂直居中
- 文字默认是基线（大部分字体是文字底部）对齐，可以通过设置vertical-align:"middle" 来实现居中对齐
- 文字的底部和顶部 是不等于底线和顶线的
- inline图片下边会有空隙：不是底线对齐，而是基线对齐。解决方法：设置vertical-align:"bottom" 底线对齐 /设置display为block，独占一行，同样就不会有间隙了

### 背景

- 背景颜色
    
    - background: 少用英文单词
    - rgb16进制表示法： #FF0000 -> 每两位相同可简写为 #F00
    - hsl表示法：hsl(色相0-360，饱和度0-100%，亮度0-100%, optional: 透明度0-1)
    - background:url(路径) 

- 渐变色背景
    
    - 老写法: `background: -webkit-linear-gradient(开始位置（’left‘），颜色1，颜色2)`
    - 新写法： `background: linear-gradient(to 开始位置（’to left‘），颜色1，颜色2)`
    - `background: linear-gradient(角度(0deg)，颜色1，颜色2)`
        - 0deg: 从下到上
        - 45deg: 从左下到右上
        - 90deg: 从左到右
        - 180deg: 从上到下
    - `background: linear-gradient(角度(0deg)，颜色1 出现的位置，颜色2 出现的位置， ...)`
        - eg: `background: linear-gradient(135deg, red 0, green 10%, blue 100%)`
    - 可以设置透明
        - eg: `background: linear-gradient(135deg, transparent 0, transparent 49.5%, green 49.5%, green 50.5%, transparent 50.5%, transparent 100%,)` 这是一条斜线
    - 设置背景大小： `background-size: 30px 30px ` 平铺满

- 多背景叠加
    
    - 交叉网格线
   
    ```CSS
    background: linear-gradient(135deg, transparent 0, transparent 49.5%, green 49.5%, green 50.5%, transparent 50.5%, transparent 100%,)；
         linear-gradient(45deg, transparent 0, transparent 49.5%, red 49.5%, red 50.5%, transparent 50.5%, transparent 100%,)；
    ```
    
- 背景图片和属性（雪碧图）
    
    - 属性：
        
        - background 背景色的背景图叠加不需要逗号
        - `background: red url(./xxx.png)` 默认平铺
        - `background-repeat: no-repeat` 不平铺 `repeat-x` x方向平铺
        - `background-position: center center` 中间显示
        - `background-position: 20px 30px` 距左20 距右30
        - `background-size: 100px 50px` resize to 100px*50pz
            - 要缩小图片
            - 在适配移动端的时候： 1个像素对应多个屏幕实际像素，缩小图片来适应
   
    - 雪碧图
        
        - 将所有图标放在一张图上，减少HTTP请求次数
        - 通过`background-position: -20px -30px` 和 `width: __px; height:__px` 调整要显示的图标

- base64和性能优化
    
    - 可以用base64码，替换路径，来显示图片
    - 一般用在小icon上
    - 优点：减少HTTP连接数
    - 缺点：图片体积扩大至4/3，导致CSS过大。 解码开销变大。

### 边框

- 属性：线型，大小，颜色
- 边框背景图
- 边框衔接（三角形）

- 属性
    - `border: 1px solid red` 一个像素实线红色边框
    - 线型： solid dotted dashed

- 边框背景图
    - `border-img: url(路径) 像素 效果`
    - 效果： 默认：拉伸 / repeat: 重复with不完整图形 / round: 重复完整图形
    
- 三角形衔接
    - border边与边斜着衔接
    - 用边框实现一个三角形， 底broder宽， 左右border透明

### 滚动

- 滚动行为和滚动条
    
    ![](https://i.imgur.com/M8UssqX.png)
    
### 文字折行

- overflow-warp(旧：word-warp) 通用换行控制
    - 是否保留单词
- word-break 针对对字节文字
    - 单词为单位 or 字母为单位
- white-space 在空白处是否断行

**Usage: 可以灵活组合**
- overflow-warp
    - normal(默认， 单词不换行)
    - break-word（单词可拆，换行， 但是单词还是一个单位）
- word-break
    - normal(默认)
    - break-all（单词不再当做一个单位）
    - keep-all (所有的单词都是一个单位， 中文的句子也是一个单位) 
- white-space
    - normal
    - nowrap 无换行

### 装饰性属性及其他

- 字重（粗体）font-weight
    - normal 默认
    - bold
    - bolder 更粗
    - lighter 
    - 数字 100 - 900(只能百位数) （eg: 100）
        - normal 一般是 400
        - bold 一般是 700
        - bolder 和 lighter 由父级确定
- 斜体 font-style: itatic
- 下划线 text-decotation
- 指针 cursor


### CSS Hack

- 兼容 IE
- Hack 即不合法但生效的写法
- 主要用于区分不同浏览器
- 缺点： 难理解 难维护 易失效
- 替代方案：特性检测 针对性的加class
- 写hack时，标准属性在前面，特殊属性写后边

