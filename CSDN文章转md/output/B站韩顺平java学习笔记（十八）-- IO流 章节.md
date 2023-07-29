**目录**

一 文件

1 文件流

2 创建文件对象相关构造器和方法

（1）相关方法

（2）应用实例

3 常用的文件操作

（1）获取文件的相关信息

（2）目录的操作和文件删除

二 IO流原理及流的处理

1 Java IO流原理

2 流的分类

3 IO流体系图-常用的类

（1）IO流体系图

（2）文件VS流

（3）InputStream（字节输入流）常用的子类

（4）OutputStream（字节输出流）常用的子类

（5）ObjectInputStream和ObjectOutputStream

（6）文件拷贝

（7）FileReader 和 FileWriter 介绍

三 节点流和处理流

1 基本介绍

2 节点流和处理流一览图

3 区别和联系

​4 处理流-BufferedReader 和 BufferedWriter

（1）BufferedReader读取文本文件

（2）BufferedWriter写入文本文件

（3）BufferedWriter和BufferedReader合用

5 处理流-BufferedInputStream 和 BufferedOutputStream

（1）介绍 BufferedInputStream

（2）介绍 BufferedOutputStream

（3）BufferedInputStream和BufferedOutputStream应用实例

四 标准输入流与输出流

1 标准输入输出流

五 转换流

1 介绍

2 应用实例

六 打印流

1 PrintStream（字节打印流）

2 PrintWriter（字符打印流）

七 Properties类

1 基本介绍

（1）专门用于读写配置文件的集合类

（2）注意事项

（3）Properties的常见方法

2 应用实例

（1）传统方法

（2）properties类方法

* * *

# 一 文件

文件是保存数据的地方。

## 1 文件流

文件在程序中是以流的形式来操作的。

![](https://img-blog.csdnimg.cn/adf497d631fe4ee4b1ba7251ad891b4f.png?x-oss-
process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aWI5pav5p2O5YWI55Sf,size_19,color_FFFFFF,t_70,g_se,x_16)

流：数据在数据源（文件）和程序（内存）之间经历的路径；

输入流：数据从数据源（文件）到程序（内存）的路径；

输出流：数据从程序（内存）到数据源（文件）的路径。

## 2 创建文件对象相关构造器和方法

![](https://img-blog.csdnimg.cn/a62db3db08a54f7bb37af74bc9b1bb7a.png?x-oss-
process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aWI5pav5p2O5YWI55Sf,size_12,color_FFFFFF,t_70,g_se,x_16)

![](https://img-blog.csdnimg.cn/07ccb499d608415ca5b15f0837cb4f71.png?x-oss-
process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aWI5pav5p2O5YWI55Sf,size_7,color_FFFFFF,t_70,g_se,x_16)

### （1）相关方法

① new File(String pathname) //根据路径构建一个File对象；

② new File(File parent,String child) //根据父目录文件+子路径构建一个File对象；

③ new File(String parent,String child) //根据父目录+子路径构建一个File对象；

④ 使用createNewFile创建新文件。

### （2）应用实例

    
    
    public class FileCreate {
        public static void main(String[] args) {
    
        }
    
        //方式1 new File(String pathname)
        @Test
        public void create01() {
            String filePath = "e:\\news1.txt";
            File file = new File(filePath);
    
            try {
                file.createNewFile();
                System.out.println("文件创建成功");
            } catch (IOException e) {
                e.printStackTrace();
            }
    
        }
        //方式2 new File(File parent,String child) //根据父目录文件+子路径构建
        //e:\\news2.txt
        @Test
        public  void create02() {
            File parentFile = new File("e:\\");
            String fileName = "news2.txt";
            //这里的file对象，在java程序中，只是一个对象
            //只有执行了createNewFile 方法，才会真正的，在磁盘创建该文件
            File file = new File(parentFile, fileName);
    
            try {
                file.createNewFile();
                System.out.println("创建成功~");
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    
        //方式3 new File(String parent,String child) //根据父目录+子路径构建
        @Test
        public void create03() {
            //String parentPath = "e:\\";
            String parentPath = "e:\\";
            String fileName = "news4.txt";
            File file = new File(parentPath, fileName);
    
            try {
                file.createNewFile();
                System.out.println("创建成功~");
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    
        //下面四个都是抽象类
        //
        //InputStream
        //OutputStream
        //Reader //字符输入流
        //Writer  //字符输出流
    }

## 3 常用的文件操作

### （1）获取文件的相关信息

    
    
    public class FileInformation {
        public static void main(String[] args) {
    
        }
    
        //获取文件的信息
        @Test
        public void info() {
            //先创建文件对象
            File file = new File("e:\\news1.txt");
    
            //调用相应的方法，得到对应信息
            System.out.println("文件名字=" + file.getName());
            //getName、getAbsolutePath、getParent、length、exists、isFile、isDirectory
            System.out.println("文件绝对路径=" + file.getAbsolutePath());
            System.out.println("文件父级目录=" + file.getParent());
            System.out.println("文件大小(字节)=" + file.length());
            //按字节计算，utf-8编码下，一个英文字母一个字节，一个汉字三个字节
            System.out.println("文件是否存在=" + file.exists());//T
            System.out.println("是不是一个文件=" + file.isFile());//T
            System.out.println("是不是一个目录=" + file.isDirectory());//F
    
    
        }
    }
    

###  （2）目录的操作和文件删除

mkdir创建一级目录，mkdirs创建多级目录，delete删除空目录或文件【注意如果目录下有文件或者目录，则不能删除，只能将其内清空才能删除】。

    
    
    public class Directory_ {
        public static void main(String[] args) {
    
            
        }
    
        //判断 d:\\news1.txt 是否存在，如果存在就删除
        @Test
        public void m1() {
    
            String filePath = "e:\\news1.txt";
            File file = new File(filePath);
            if (file.exists()) {
                if (file.delete()) {
                    System.out.println(filePath + "删除成功");
                } else {
                    System.out.println(filePath + "删除失败");
                }
            } else {
                System.out.println("该文件不存在...");
            }
    
        }
    
        //判断 D:\\demo02 是否存在，存在就删除，否则提示不存在
        //这里我们需要体会到，在java编程中，目录也被当做文件
        @Test
        public void m2() {
    
            String filePath = "D:\\demo02";
            File file = new File(filePath);
            if (file.exists()) {
                if (file.delete()) {
                    System.out.println(filePath + "删除成功");
                } else {
                    System.out.println(filePath + "删除失败");
                }
            } else {
                System.out.println("该目录不存在...");
            }
    
        }
    
        //判断 D:\\demo\\a\\b\\c 目录是否存在，如果存在就提示已经存在，否则就创建
        @Test
        public void m3() {
    
            String directoryPath = "D:\\demo\\a\\b\\c";
            File file = new File(directoryPath);
            if (file.exists()) {
                System.out.println(directoryPath + "存在..");
            } else {
                if (file.mkdirs()) { //创建一级目录使用mkdir() ，创建多级目录使用mkdirs()
                    System.out.println(directoryPath + "创建成功..");
                } else {
                    System.out.println(directoryPath + "创建失败...");
                }
            }
        }
        //判断 D:\\demo 目录是否存在，如果存在就提示已经存在，否则就创建
        @Test
        public void m4() {
    
            String directoryPath = "D:\\demo";
            File file = new File(directoryPath);
            if (file.exists()) {
                System.out.println(directoryPath + "存在..");
            } else {
                if (file.mkdir()) { //创建一级目录使用mkdir() ，创建多级目录使用mkdirs()
                    System.out.println(directoryPath + "创建成功..");
                } else {
                    System.out.println(directoryPath + "创建失败...");
                }
            }
        }
    }

# 二 IO流原理及流的处理

## 1 Java IO流原理

（1）I/O是Input/Output的缩写，I/O技术是非常实用的技术，用于处理数据传输。如读/写文件，网络通讯等；

（2）Java程序中，对于数据的输入/输出操作以“流（stream）”的方式进行；

（3）java.io包下提供了各种“流”类和接口，用以获取不同种类的数据，并通过方法输入或输出数据；

（4）输入input：读取外部数据（磁盘，光盘等存储设备的数据）到程序（内存）中；

（5）输出output：将程序（内存）数据输出到磁盘，光盘等存储设备中。

![](https://img-blog.csdnimg.cn/a00688d6846e4e9c9536a652a5b93fe4.png?x-oss-
process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aWI5pav5p2O5YWI55Sf,size_13,color_FFFFFF,t_70,g_se,x_16)

##  2 流的分类

（1）按照操作数据单位不同分为：字节流（8bit）【便于处理二进制文件】，字符流（按字符）【便于处理文本文件】；

（2）按数据流的流入不同分为：输入流，输出流；

（3）按流的角色的不同分为：节点流，处理流/包装流。

![](https://img-blog.csdnimg.cn/0e63522377ec49f598ca6d64dcad1f4f.png?x-oss-
process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aWI5pav5p2O5YWI55Sf,size_19,color_FFFFFF,t_70,g_se,x_16)

① Java的IO流共涉及40多个类，实际上非常规则，都是从如上4个抽象基类派生的；

② 由这四个类派生出来的子类名称都是以其父类名作为子类名后缀。

## 3 IO流体系图-常用的类

### （1）IO流体系图

![](https://img-blog.csdnimg.cn/71e05d0284df419181f1c27a5d4d540b.png?x-oss-
process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aWI5pav5p2O5YWI55Sf,size_19,color_FFFFFF,t_70,g_se,x_16)

### （2）文件VS流

![](https://img-blog.csdnimg.cn/adf497d631fe4ee4b1ba7251ad891b4f.png?x-oss-
process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aWI5pav5p2O5YWI55Sf,size_19,color_FFFFFF,t_70,g_se,x_16)

### （3） InputStream（字节输入流）常用的子类

![](https://img-blog.csdnimg.cn/8147e6930580495c819e3559ee11fc39.png?x-oss-
process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aWI5pav5p2O5YWI55Sf,size_20,color_FFFFFF,t_70,g_se,x_16)**FileInputStream：文件输入流**

![](https://img-blog.csdnimg.cn/776c6876b8ec47778e437ed38afa7c20.png?x-oss-
process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aWI5pav5p2O5YWI55Sf,size_20,color_FFFFFF,t_70,g_se,x_16)

**应用实例**

![](https://img-blog.csdnimg.cn/bf4a32c3c81a4d7790ee43bd8759eff4.png?x-oss-
process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aWI5pav5p2O5YWI55Sf,size_20,color_FFFFFF,t_70,g_se,x_16)

    
    
    public class FileInputStream_ {
        public static void main(String[] args) {
    
        }
    
        /**
         * 演示读取文件...
         * 单个字节的读取，效率比较低
         * -> 使用 read(byte[] b)
         */
        @Test
        public void readFile01() {
            String filePath = "e:\\hello.txt";
            int readData = 0;
            FileInputStream fileInputStream = null;
            try {
                //创建 FileInputStream 对象，用于读取 文件
                fileInputStream = new FileInputStream(filePath);
                //从该输入流读取一个字节的数据。 如果没有输入可用，此方法将阻止。
                //如果返回-1 , 表示读取完毕
                while ((readData = fileInputStream.read()) != -1) {
                    System.out.print((char)readData);//转成char显示
                }
    
            } catch (IOException e) {
                e.printStackTrace();
            } finally {
                //关闭文件流，释放资源.
                try {
                    fileInputStream.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
    
        }
    
        /**
         * 使用 read(byte[] b) 读取文件，提高效率
         */
        @Test
        public void readFile02() {
            String filePath = "e:\\hello.txt";
            //字节数组
            byte[] buf = new byte[8]; //一次读取8个字节.
            int readLen = 0;
            FileInputStream fileInputStream = null;
            try {
                //创建 FileInputStream 对象，用于读取 文件
                fileInputStream = new FileInputStream(filePath);
                //从该输入流读取最多b.length字节的数据到字节数组。 此方法将阻塞，直到某些输入可用。
                //如果返回-1 , 表示读取完毕
                //如果读取正常, 返回实际读取的字节数
                while ((readLen = fileInputStream.read(buf)) != -1) {
                    System.out.print(new String(buf, 0, readLen));//显示
                }
    
            } catch (IOException e) {
                e.printStackTrace();
            } finally {
                //关闭文件流，释放资源.
                try {
                    fileInputStream.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
    
        }
    }
    

### （4） OutputStream（字节输出流）常用的子类

![](https://img-blog.csdnimg.cn/c3bab8c052574f8392a3fc41c9edda58.png?x-oss-
process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aWI5pav5p2O5YWI55Sf,size_14,color_FFFFFF,t_70,g_se,x_16)

**FileOutStream：文件输出流**

![](https://img-blog.csdnimg.cn/5f4038bf36ad44a59b67ab3bec745ef4.png?x-oss-
process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aWI5pav5p2O5YWI55Sf,size_19,color_FFFFFF,t_70,g_se,x_16)

**应用实例 一**

![](https://img-blog.csdnimg.cn/364f852a57434d94a9def5c3a2858ca3.png?x-oss-
process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aWI5pav5p2O5YWI55Sf,size_20,color_FFFFFF,t_70,g_se,x_16)

    
    
    public class FileOutputStream01 {
        public static void main(String[] args) {
    
        }
    
        /**
         * 演示使用FileOutputStream 将数据写到文件中,
         * 如果该文件不存在，则创建该文件
         */
        @Test
        public void writeFile() {
    
            //创建 FileOutputStream对象
            String filePath = "e:\\a.txt";
            FileOutputStream fileOutputStream = null;
            try {
                //得到 FileOutputStream对象 对象
                //老师说明
                //1. new FileOutputStream(filePath) 创建方式，当写入内容是，会覆盖原来的内容
                //2. new FileOutputStream(filePath, true) 创建方式，当写入内容是，是追加到文件后面
                fileOutputStream = new FileOutputStream(filePath, true);
                //写入一个字节
                //fileOutputStream.write('H');//
                //写入字符串
                String str = "hsp,world!";
                //str.getBytes() 可以把 字符串-> 字节数组
                //fileOutputStream.write(str.getBytes());
                /*
                write(byte[] b, int off, int len) 将 len字节从位于偏移量 off的指定字节数组写入此文件输出流
                 */
                fileOutputStream.write(str.getBytes(), 0, 3);
    
            } catch (IOException e) {
                e.printStackTrace();
            } finally {
                try {
                    fileOutputStream.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
    

### （5）ObjectInputStream和ObjectOutputStream

① 功能：提供了对基本类型或对象类型的序列化和反序列化的方法；

② **** ObjectOutputStream 提供 序列化功能；

③ **** ObjectInputStream 提供 反序列化功能。

![](https://img-blog.csdnimg.cn/8e90c16fc132465f931a2d7083f80732.png?x-oss-
process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aWI5pav5p2O5YWI55Sf,size_20,color_FFFFFF,t_70,g_se,x_16)

![](https://img-blog.csdnimg.cn/e6f0efc07b0448708eb064cc576ac672.png?x-oss-
process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aWI5pav5p2O5YWI55Sf,size_20,color_FFFFFF,t_70,g_se,x_16)

优先使用Serializable接口，因为这个接口没有方法。

**ObjectInputStream：对象输入流**

![](https://img-blog.csdnimg.cn/3b2a1efd8e714e7db72ccd20289b036e.png?x-oss-
process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aWI5pav5p2O5YWI55Sf,size_20,color_FFFFFF,t_70,g_se,x_16)

**ObjectOutputStream：对象输出流**

![](https://img-blog.csdnimg.cn/d5bb6620ac54402daa87e7355d872206.png?x-oss-
process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aWI5pav5p2O5YWI55Sf,size_20,color_FFFFFF,t_70,g_se,x_16)

**应用实例：**

**用ObjectOutputStream序列化，然后用ObjectInputStream反序列化数据。**

    
    
    //ObjectOutStream_类
    public class ObjectOutStream_ {
        public static void main(String[] args) throws Exception {
            //序列化后，保存的文件格式，不是存文本，而是按照他的格式来保存
            String filePath = "e:\\data.dat";
    
            ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(filePath));
    
            //序列化数据到 e:\data.dat
            oos.writeInt(100);// int -> Integer (实现了 Serializable)
            oos.writeBoolean(true);// boolean -> Boolean (实现了 Serializable)
            oos.writeChar('a');// char -> Character (实现了 Serializable)
            oos.writeDouble(9.5);// double -> Double (实现了 Serializable)
            oos.writeUTF("韩顺平教育");//String
            //保存一个dog对象
            oos.writeObject(new Dog("旺财", 10));
            oos.close();
            System.out.println("数据保存完毕(序列化形式)");
    
    
        }
    }
    
    
    
    //如果需要序列化某个类的对象，实现 Serializable
    public class Dog implements Serializable {
        private String name;
        private int age;
       
    
        public Dog(String name, int age) {
            this.name = name;
            this.age = age;
        }
    
        @Override
        public String toString() {
            return "Dog{" +
                    "name='" + name + '\'' +
                    ", age=" + age;
        }
    
        public String getName() {
            return name;
        }
    
        public void setName(String name) {
            this.name = name;
        }
    
        public int getAge() {
            return age;
        }
    
        public void setAge(int age) {
            this.age = age;
        }
    }
    
    
    // ObjectInputStream_类
    public class ObjectInputStream_ {
        public static void main(String[] args) throws IOException, ClassNotFoundException {
    
            //指定反序列化的文件
            String filePath = "e:\\data.dat";
    
            ObjectInputStream ois = new ObjectInputStream(new FileInputStream(filePath));
    
            //读取
            //老师解读
            //1. 读取(反序列化)的顺序需要和你保存数据(序列化)的顺序一致
            //2. 否则会出现异常
    
            System.out.println(ois.readInt());
            System.out.println(ois.readBoolean());
    
            System.out.println(ois.readChar());
            System.out.println(ois.readDouble());
            System.out.println(ois.readUTF());
    
    
            //dog 的编译类型是 Object , dog 的运行类型是 Dog
            Object dog = ois.readObject();
            System.out.println("运行类型=" + dog.getClass());
            System.out.println("dog信息=" + dog);//底层 Object -> Dog
    
            //这里是特别重要的细节:
    
            //1. 如果我们希望调用Dog的方法, 需要向下转型
            //2. 需要我们将Dog类的定义，放在到可以引用的位置
            Dog dog2 = (Dog)dog;
            System.out.println(dog2.getName()); //旺财..
    
            //关闭流, 关闭外层流即可，底层会关闭 FileInputStream 流
            ois.close();
    
    
        }
    }
    
    

**注意事项和使用细节**

![](https://img-blog.csdnimg.cn/badd12827c044c519103767872fb8952.png?x-oss-
process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aWI5pav5p2O5YWI55Sf,size_20,color_FFFFFF,t_70,g_se,x_16)

    
    
    //如果需要序列化某个类的对象，实现 Serializable
    public class Dog implements Serializable {
        private String name;
        private int age;
        //序列化对象时，默认将里面所有属性都进行序列化，但除了static或transient修饰的成员
        private static String nation;
        private transient String color;
        //序列化对象时，要求里面属性的类型也需要实现序列化接口
        private Master master = new Master();
    
        //serialVersionUID 序列化的版本号，可以提高兼容性
        private static final long serialVersionUID = 1L;
    
        public Dog(String name, int age, String nation, String color) {
            this.name = name;
            this.age = age;
            this.color = color;
            this.nation = nation;
        }
    
        @Override
        public String toString() {
            return "Dog{" +
                    "name='" + name + '\'' +
                    ", age=" + age +
                    ", color='" + color + '\'' +
                    '}' + nation + " " +master;
        }
    
        public String getName() {
            return name;
        }
    
        public void setName(String name) {
            this.name = name;
        }
    
        public int getAge() {
            return age;
        }
    
        public void setAge(int age) {
            this.age = age;
        }
    }

### （6）文件拷贝

编辑完成图片/音乐的拷贝。

    
    
    public class FileCopy {
        public static void main(String[] args) {
            //完成 文件拷贝，将 e:\\Koala.jpg 拷贝 c:\\
            //思路分析
            //1. 创建文件的输入流 , 将文件读入到程序
            //2. 创建文件的输出流， 将读取到的文件数据，写入到指定的文件.
            String srcFilePath = "e:\\Koala.jpg";
            String destFilePath = "e:\\Koala3.jpg";
            FileInputStream fileInputStream = null;
            FileOutputStream fileOutputStream = null;
    
            try {
    
                fileInputStream = new FileInputStream(srcFilePath);
                fileOutputStream = new FileOutputStream(destFilePath);
                //定义一个字节数组,提高读取效果
                byte[] buf = new byte[1024];
                int readLen = 0;
                while ((readLen = fileInputStream.read(buf)) != -1) {
                    //读取到后，就写入到文件 通过 fileOutputStream
                    //即，是一边读，一边写
                    fileOutputStream.write(buf, 0, readLen);//一定要使用这个方法，
                    //fileOutputStream.write(buf);如果有的不满一个数组的话，
                    //就会出现将空的null也传过去，可能会出现打不开图片的情况。
    
                }
                System.out.println("拷贝ok~");
    
    
            } catch (IOException e) {
                e.printStackTrace();
            } finally {
                try {
                    //关闭输入流和输出流，释放资源
                    if (fileInputStream != null) {
                        fileInputStream.close();
                    }
                    if (fileOutputStream != null) {
                        fileOutputStream.close();
                    }
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
    
    
        }
    }
    

###  （7）FileReader 和 FileWriter 介绍

FileReader 和 FileWriter 是字符流，即按照字符来操作IO。

**① FileReader**

![](https://img-blog.csdnimg.cn/2b8114b2c0d145798e5beabeffc2fc40.png?x-oss-
process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aWI5pav5p2O5YWI55Sf,size_11,color_FFFFFF,t_70,g_se,x_16)

**FileReader相关方法：**

![](https://img-blog.csdnimg.cn/8548780a33a6462b851519237aab77b1.png?x-oss-
process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aWI5pav5p2O5YWI55Sf,size_20,color_FFFFFF,t_70,g_se,x_16)

**相关API：**

![](https://img-blog.csdnimg.cn/892526b7e6d14c95b18023894161504f.png?x-oss-
process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aWI5pav5p2O5YWI55Sf,size_20,color_FFFFFF,t_70,g_se,x_16)

**应用实例：**

![](https://img-blog.csdnimg.cn/2037b1c960ee443b9430319b1c978a98.png?x-oss-
process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aWI5pav5p2O5YWI55Sf,size_19,color_FFFFFF,t_70,g_se,x_16)

    
    
        public class FileReader_ {
        public static void main(String[] args) {
    
    
        }
    
        /**
         * 单个字符读取文件
         */
        @Test
        public void readFile01() {
            String filePath = "e:\\story.txt";
            FileReader fileReader = null;
            int data = 0;
            //1. 创建FileReader对象
            try {
                fileReader = new FileReader(filePath);
                //循环读取 使用read, 单个字符读取
                while ((data = fileReader.read()) != -1) {
                    System.out.print((char) data);
                }
    
            } catch (IOException e) {
                e.printStackTrace();
            } finally {
                try {
                    if (fileReader != null) {
                        fileReader.close();
                    }
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    
        /**
         * 字符数组读取文件
         */
        @Test
        public void readFile02() {
            System.out.println("~~~readFile02 ~~~");
            String filePath = "e:\\story.txt";
            FileReader fileReader = null;
    
            int readLen = 0;
            char[] buf = new char[8];
            //1. 创建FileReader对象
            try {
                fileReader = new FileReader(filePath);
                //循环读取 使用read(buf), 返回的是实际读取到的字符数
                //如果返回-1, 说明到文件结束
                while ((readLen = fileReader.read(buf)) != -1) {
                    System.out.print(new String(buf, 0, readLen));
                }
    
            } catch (IOException e) {
                e.printStackTrace();
            } finally {
                try {
                    if (fileReader != null) {
                        fileReader.close();
                    }
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    
    }
    

**② FileWriter**

![](https://img-blog.csdnimg.cn/611f08f1acfa440c9cd67a36f24a646b.png?x-oss-
process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aWI5pav5p2O5YWI55Sf,size_20,color_FFFFFF,t_70,g_se,x_16)

**FileWriter相关方法：**

![](https://img-blog.csdnimg.cn/671cc11ca7e841d484c256170422b9d0.png?x-oss-
process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aWI5pav5p2O5YWI55Sf,size_20,color_FFFFFF,t_70,g_se,x_16)

**相关API：**

![](https://img-blog.csdnimg.cn/6791215074e046a2b1b0e5718de6656b.png?x-oss-
process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aWI5pav5p2O5YWI55Sf,size_18,color_FFFFFF,t_70,g_se,x_16)

**注意：**

![](https://img-blog.csdnimg.cn/efaf95065ea94ae091df5268fdc696d6.png?x-oss-
process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aWI5pav5p2O5YWI55Sf,size_20,color_FFFFFF,t_70,g_se,x_16)

**应用实例：**

![](https://img-blog.csdnimg.cn/f6eaf88ba4a748488fe39e485736e99a.png?x-oss-
process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aWI5pav5p2O5YWI55Sf,size_20,color_FFFFFF,t_70,g_se,x_16)

    
    
    public class FileWriter_ {
        public static void main(String[] args) {
    
            String filePath = "e:\\note.txt";
            //创建FileWriter对象
            FileWriter fileWriter = null;
            char[] chars = {'a', 'b', 'c'};
            try {
                fileWriter = new FileWriter(filePath);//默认是覆盖写入
    //            3) write(int):写入单个字符
                fileWriter.write('H');
    //            4) write(char[]):写入指定数组
                fileWriter.write(chars);
    //            5) write(char[],off,len):写入指定数组的指定部分
                fileWriter.write("韩顺平教育".toCharArray(), 0, 3);
    //            6) write（string）：写入整个字符串
                fileWriter.write(" 你好北京~");
                fileWriter.write("风雨之后，定见彩虹");
    //            7) write(string,off,len):写入字符串的指定部分
                fileWriter.write("上海天津", 0, 2);
                //在数据量大的情况下，可以使用循环操作.
    
    
            } catch (IOException e) {
                e.printStackTrace();
            } finally {
    
                //对应FileWriter , 一定要关闭流，或者flush才能真正的把数据写入到文件
                //老韩看源码就知道原因.
                /*
                    看看代码
                    private void writeBytes() throws IOException {
            this.bb.flip();
            int var1 = this.bb.limit();
            int var2 = this.bb.position();
    
            assert var2 <= var1;
    
            int var3 = var2 <= var1 ? var1 - var2 : 0;
            if (var3 > 0) {
                if (this.ch != null) {
                    assert this.ch.write(this.bb) == var3 : var3;
                } else {
                    this.out.write(this.bb.array(), this.bb.arrayOffset() + var2, var3);
                }
            }
    
            this.bb.clear();
        }
                 */
                try {
                    //fileWriter.flush();
                    //关闭文件流，等价 flush() + 关闭
                    fileWriter.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
    
            }
    
            System.out.println("程序结束...");
    
    
        }
    }
    

# 三 节点流和处理流

## 1 基本介绍

（1）节点流可以从一个特定的数据源【数据源就是存放数据的地方】读写数据，如FileReader、FileWriter；

![](https://img-blog.csdnimg.cn/69fe3381b79c4190a16f975f27fc859e.png?x-oss-
process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aWI5pav5p2O5YWI55Sf,size_20,color_FFFFFF,t_70,g_se,x_16)

（2）处理流（也叫包装流）是“连接”在已存在的流（节点流或处理流）之上，为程序提供更为强大的读写功能，也更加灵活，如BufferedReader、BufferedWriter。

处理流例如BufferedReader类中，有属性Reader，既可以封装一个节点流，该节点流可以是任意的，只要是Reader子类。

![](https://img-blog.csdnimg.cn/cb605b66d38d448eb710b82b794c6fd3.png?x-oss-
process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aWI5pav5p2O5YWI55Sf,size_11,color_FFFFFF,t_70,g_se,x_16)

![](https://img-blog.csdnimg.cn/56dcd3cd45cf4af4ada62f0292c71cdf.png?x-oss-
process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aWI5pav5p2O5YWI55Sf,size_16,color_FFFFFF,t_70,g_se,x_16)

##  2 节点流和处理流一览图

![](https://img-blog.csdnimg.cn/47cf739daff04f479add3e13a9587411.png?x-oss-
process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aWI5pav5p2O5YWI55Sf,size_20,color_FFFFFF,t_70,g_se,x_16)

## 3 区别和联系

（1）节点流是底层流/低级流，直接跟数据源相接；

（2）处理流包装节点流，既可以消除不同节点流的实现差异，也可以提供更方便的方法来实现输入输出；

（3）处理流（包装流）对节点流进行包装，使用了 修饰器设计模式，不会直接于数据源相连。

**模拟修饰器设计模式**

    
    
    //Reader_类
    public abstract class Reader_ { //抽象类
        public void readFile() {
        }
        public void readString() {
        }
    
        //在Reader_ 抽象类，使用read方法统一管理.
        //后面在调用时，利于对象动态绑定机制， 绑定到对应的实现子类即可.
        //public abstract void read();
    }
    
    
    //FileReader_类
    public class FileReader_ extends Reader_ {
    
            public void readFile() {
            System.out.println("对文件进行读取...");
        }
    }
    
    
    // StringReader_类
    public class StringReader_ extends Reader_ {
        public void readString() {
            System.out.println("读取字符串..");
        }
    
    }
    
    
    
    // BufferedReader_类
    public class BufferedReader_ extends Reader_{
    
        private Reader_ reader_; //属性是 Reader_类型
    
        //接收Reader_ 子类对象
        public BufferedReader_(Reader_ reader_) {
            this.reader_ = reader_;
        }
    
        public void readFile() { //封装一层
            reader_.readFile();
        }
    
        //让方法更加灵活， 多次读取文件, 或者加缓冲byte[] ....
        public void readFiles(int num) {
            for(int i = 0; i < num; i++) {
                reader_.readFile();
            }
        }
    
        //扩展 readString, 批量处理字符串数据
        public void readStrings(int num) {
            for(int i = 0; i 
    
    
    //Test_类
    public class Test_ {
        public static void main(String[] args) {
    
    
            BufferedReader_ bufferedReader_ = new BufferedReader_(new FileReader_());
            bufferedReader_.readFiles(10);
            //bufferedReader_.readFile();
            //Serializable
            //Externalizable
            //ObjectInputStream
            //ObjectOutputStream
            //这次希望通过 BufferedReader_ 多次读取字符串
            BufferedReader_ bufferedReader_2 = new BufferedReader_(new StringReader_());
            bufferedReader_2.readStrings(5);
        }
    }

## ![](https://img-blog.csdnimg.cn/aad3aef5a9494919806294ce88bf181b.png?x-oss-
process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aWI5pav5p2O5YWI55Sf,size_20,color_FFFFFF,t_70,g_se,x_16)
4 处理流-BufferedReader 和 BufferedWriter

**注意：**
BufferedReader和BufferedWriter属于字符流，是按照字符来读取数据的，关闭时，只需要关闭外层流即可。【因为底层会调用的处理流传入的字节流的close方法】

### （1）BufferedReader读取文本文件

    
    
    public class BufferedReader_ {
        public static void main(String[] args) throws Exception {
    
            String filePath = "e:\\a.java";
            //创建bufferedReader
            BufferedReader bufferedReader = new BufferedReader(new FileReader(filePath));
            //读取
            String line; //按行读取, 效率高
            //说明
            //1. bufferedReader.readLine() 是按行读取文件
            //2. 当返回null 时，表示文件读取完毕
            while ((line = bufferedReader.readLine()) != null) {
                System.out.println(line);
            }
    
            //关闭流, 这里注意，只需要关闭 BufferedReader ，因为底层会自动的去关闭 节点流
            //FileReader。
            /*
                public void close() throws IOException {
                    synchronized (lock) {
                        if (in == null)
                            return;
                        try {
                            in.close();//in 就是我们传入的 new FileReader(filePath), 关闭了.
                        } finally {
                            in = null;
                            cb = null;
                        }
                    }
                }
    
             */
            bufferedReader.close();
    
        }
    }

### （2）BufferedWriter写入文本文件

    
    
    public class BufferedWriter_ {
        public static void main(String[] args) throws IOException {
            String filePath = "e:\\ok.txt";
            //创建BufferedWriter
            //说明:
            //1. new FileWriter(filePath, true) 表示以追加的方式写入
            //2. new FileWriter(filePath) , 表示以覆盖的方式写入
            BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(filePath));
            bufferedWriter.write("hello, world!");
            bufferedWriter.newLine();//插入一个和系统相关的换行
            bufferedWriter.write("hello2, world!");
            bufferedWriter.newLine();
            bufferedWriter.write("hello3, world!");
            bufferedWriter.newLine();
    
            //说明：关闭外层流即可 ， 传入的 new FileWriter(filePath) ,会在底层关闭
            bufferedWriter.close();
    
        }
    }

###  （3）BufferedWriter和BufferedReader合用

进行文本文件的拷贝。

    
    
    public class BufferedCopy_ {
    
        public static void main(String[] args) {
    
    
            //说明
            //1. BufferedReader 和 BufferedWriter 是安装字符操作
            //2. 不要去操作 二进制文件[声音，视频，doc, pdf ], 可能造成文件损坏
            //BufferedInputStream
            //BufferedOutputStream
            String srcFilePath = "e:\\a.java";
            String destFilePath = "e:\\a2.java";
    //        String srcFilePath = "e:\\0245_韩顺平零基础学Java_引出this.avi";
    //        String destFilePath = "e:\\a2韩顺平.avi";
            BufferedReader br = null;
            BufferedWriter bw = null;
            String line;
            try {
                br = new BufferedReader(new FileReader(srcFilePath));
                bw = new BufferedWriter(new FileWriter(destFilePath));
    
                //说明: readLine 读取一行内容，但是没有换行
                while ((line = br.readLine()) != null) {
                    //每读取一行，就写入
                    bw.write(line);
                    //插入一个换行
                    bw.newLine();
                }
                System.out.println("拷贝完毕...");
    
            } catch (IOException e) {
                e.printStackTrace();
            } finally {
                //关闭流
                try {
                    if(br != null) {
                        br.close();
                    }
                    if(bw != null) {
                        bw.close();
                    }
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
    
    
        }
    }

## 5 处理流-BufferedInputStream 和 BufferedOutputStream

### （1）介绍 BufferedInputStream

![](https://img-blog.csdnimg.cn/bfd2ce3146774834a9b373dd43191d4f.png?x-oss-
process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aWI5pav5p2O5YWI55Sf,size_11,color_FFFFFF,t_70,g_se,x_16)

BufferedInputStream是字节流，在创建BufferedInputStream时，会创建内部缓冲区数组。

![](https://img-blog.csdnimg.cn/63f96fec09c444b3b59c25153b906a12.png?x-oss-
process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aWI5pav5p2O5YWI55Sf,size_13,color_FFFFFF,t_70,g_se,x_16)

### （2）介绍 BufferedOutputStream

![](https://img-blog.csdnimg.cn/7be0b5b4e5264ae1adf644c20d831144.png?x-oss-
process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aWI5pav5p2O5YWI55Sf,size_10,color_FFFFFF,t_70,g_se,x_16)

BufferedOutputStream是字节流，实现缓冲的输出流，可以将多个字节写入底层输出流中，而不必对每次字节写入调用底层系统。

![](https://img-blog.csdnimg.cn/b87b12999ed2495895b203c0c80276dc.png?x-oss-
process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aWI5pav5p2O5YWI55Sf,size_15,color_FFFFFF,t_70,g_se,x_16)

###  （3）BufferedInputStream和BufferedOutputStream应用实例

    
    
    / * 思考：字节流可以操作二进制文件，可以操作文本文件吗？当然可以
     */
    public class BufferedCopy02 {
        public static void main(String[] args) {
    
    //        String srcFilePath = "e:\\Koala.jpg";
    //        String destFilePath = "e:\\hsp.jpg";
    //        String srcFilePath = "e:\\0245_韩顺平零基础学Java_引出this.avi";
    //        String destFilePath = "e:\\hsp.avi";
            String srcFilePath = "e:\\a.java";
            String destFilePath = "e:\\a3.java";
    
            //创建BufferedOutputStream对象BufferedInputStream对象
            BufferedInputStream bis = null;
            BufferedOutputStream bos = null;
    
            try {
                //因为 FileInputStream  是 InputStream 子类
                bis = new BufferedInputStream(new FileInputStream(srcFilePath));
                bos = new BufferedOutputStream(new FileOutputStream(destFilePath));
    
                //循环的读取文件，并写入到 destFilePath
                byte[] buff = new byte[1024];
                int readLen = 0;
                //当返回 -1 时，就表示文件读取完毕
                while ((readLen = bis.read(buff)) != -1) {
                    bos.write(buff, 0, readLen);
                }
    
                System.out.println("文件拷贝完毕~~~");
    
            } catch (IOException e) {
                e.printStackTrace();
            } finally {
    
                //关闭流 , 关闭外层的处理流即可，底层会去关闭节点流
                try {
                    if(bis != null) {
                        bis.close();
                    }
                    if(bos != null) {
                        bos.close();
                    }
                } catch (IOException e) {
                    e.printStackTrace();
                }
    
            }
    
    
        }
    }
    

# 四 标准输入流与输出流

## 1 标准输入输出流

| 类型| 默认设备  
---|---|---  
System.in 标准输入| InputStream| 键盘  
System.out 标准输出| PrintStream| 显示器  
      
    
    public class InputAndOutput {
        public static void main(String[] args) {
            //System 类 的 public final static InputStream in = null;
            // System.in 编译类型   InputStream
            // System.in 运行类型   BufferedInputStream
            // 表示的是标准输入 键盘
            System.out.println(System.in.getClass());
    
            //老韩解读
            //1. System.out public final static PrintStream out = null;
            //2. 编译类型 PrintStream
            //3. 运行类型 PrintStream
            //4. 表示标准输出 显示器
            System.out.println(System.out.getClass());
    
            System.out.println("hello, world~");
    
            Scanner scanner = new Scanner(System.in);
            System.out.println("输入内容");
            String next = scanner.next();
            System.out.println("next=" + next);
    
            
        }
    }
    

# 五 转换流

## 1 介绍

（1）InputStreamReader：Reader的子类，可以将InputStream（字节流）包装成（转换）Reader（字符流）；

（2）OutputStreamWriter：Writer的子类，实现将OutputStream（字节流）包装成Writer（字符流）；

（3）当处理纯文本数据时，如果使用字符流效率更高，并且可以有效解决中文问题，所以建议将字节流转换为字符流；

（4）可以在使用时指定编码格式（比如utf-8、gbk、gb2312、ISO8859-1等）。

![](https://img-blog.csdnimg.cn/c6cbb6b4476d494a82fa58fe5753fcc7.png?x-oss-
process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aWI5pav5p2O5YWI55Sf,size_16,color_FFFFFF,t_70,g_se,x_16)

![](https://img-blog.csdnimg.cn/f523e4e9f5d24a6c91905c867d841c77.png?x-oss-
process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aWI5pav5p2O5YWI55Sf,size_18,color_FFFFFF,t_70,g_se,x_16)

##  2 应用实例

如果文本文件的类型和编程软件设置的编码不一致会出现乱码的情况。

    
    
    public class CodeQuestion {
        public static void main(String[] args) throws IOException {
            //读取e:\\a.txt 文件到程序
            //思路
            //1.  创建字符输入流 BufferedReader [处理流]
            //2. 使用 BufferedReader 对象读取a.txt
            //3. 默认情况下，读取文件是按照 utf-8 编码，若不是，可能出现乱码情况。
            String filePath = "e:\\a.txt";
            BufferedReader br = new BufferedReader(new FileReader(filePath));
    
            String s = br.readLine();
            System.out.println("读取到的内容: " + s);
            br.close();
    
            //InputStreamReader
            //OutputStreamWriter
        }
    }
    
    
    /**
     * 演示使用 InputStreamReader 转换流解决中文乱码问题
     * 将字节流 FileInputStream 转成字符流  InputStreamReader, 指定编码 gbk/utf-8
     */
    public class InputStreamReader_ {
        public static void main(String[] args) throws IOException {
    
            String filePath = "e:\\a.txt";
            //解读
            //1. 把 FileInputStream 转成 InputStreamReader
            //2. 指定编码 gbk
            //InputStreamReader isr = new InputStreamReader(new FileInputStream(filePath), "gbk");
            //3. 把 InputStreamReader 传入 BufferedReader
            //BufferedReader br = new BufferedReader(isr);
    
            //将2 和 3 合在一起
            BufferedReader br = new BufferedReader(new InputStreamReader(
                                                        new FileInputStream(filePath), "gbk"));
    
            //4. 读取
            String s = br.readLine();
            System.out.println("读取内容=" + s);
            //5. 关闭外层流
            br.close();
    
        }
    
    
    }
    
    
    
    /**
     * 演示 OutputStreamWriter 使用
     * 把FileOutputStream 字节流，转成字符流 OutputStreamWriter
     * 指定处理的编码 gbk/utf-8/utf8
     */
    public class OutputStreamWriter_ {
        public static void main(String[] args) throws IOException {
            String filePath = "e:\\hsp.txt";
            String charSet = "utf-8";
            OutputStreamWriter osw = new OutputStreamWriter(new FileOutputStream(filePath), charSet);
            osw.write("hi, 哈哈哈");
            osw.close();
            System.out.println("按照 " + charSet + " 保存文件成功~");
    
    
        }
    }
    

# 六 打印流

## 1 PrintStream（字节打印流）

![](https://img-blog.csdnimg.cn/2936d1e154cb4acdb997b1b8845a75c7.png?x-oss-
process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aWI5pav5p2O5YWI55Sf,size_18,color_FFFFFF,t_70,g_se,x_16)

    
    
    /**
     * 演示PrintStream （字节打印流/输出流）
     */
    public class PrintStream_ {
        public static void main(String[] args) throws IOException {
    
            PrintStream out = System.out;
            //在默认情况下，PrintStream 输出数据的位置是 标准输出，即显示器
            /*
                 public void print(String s) {
                    if (s == null) {
                        s = "null";
                    }
                    write(s);
                }
    
             */
            out.print("john, hello");
            //因为print底层使用的是write , 所以我们可以直接调用write进行打印/输出
            out.write("韩顺平,你好".getBytes());
            out.close();
    
            //我们可以去修改打印流输出的位置/设备
            //1. 输出修改成到 "e:\\f1.txt"
            //2. "hello, 韩顺平教育~" 就会输出到 e:\f1.txt
            //3. public static void setOut(PrintStream out) {
            //        checkIO();
            //        setOut0(out); // native 方法，修改了out
            //   }
            System.setOut(new PrintStream("e:\\f1.txt"));
            System.out.println("hello, 韩顺平教育~");
    
    
        }
    }

## 2 PrintWriter（字符打印流）

![](https://img-blog.csdnimg.cn/4053750f5f9e4c3a9b7bbc3f8cffbc65.png?x-oss-
process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aWI5pav5p2O5YWI55Sf,size_20,color_FFFFFF,t_70,g_se,x_16)

    
    
    public class PrintWriter_ {
        public static void main(String[] args) throws IOException {
    
            //PrintWriter printWriter = new PrintWriter(System.out);
            PrintWriter printWriter = new PrintWriter(new FileWriter("e:\\f2.txt"));
            printWriter.print("hi, 北京你好~~~~");
            printWriter.close();//flush + 关闭流, 才会将数据写入到文件..
    
        }
    }

# 七 Properties类

## 1 基本介绍

![](https://img-blog.csdnimg.cn/a0f3781b3fcc488fa8220778ea4bf92b.png?x-oss-
process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aWI5pav5p2O5YWI55Sf,size_9,color_FFFFFF,t_70,g_se,x_16)

### （1）专门用于读写配置文件的集合类

配置文件的格式：

键=值

### （2）注意事项

键值对不需要有空格，值不需要用引号一起来，默认类型是String。

### （3）Properties的常见方法

① load：加载配置文件的键值对到Properties对象；

② list：将数据显示到指定设备；

③ getProperty(key)：根据键获取值；

④ setProperty(key,value)：设置键值对到Properties对象【没有就是新建，有就是修改】；

⑤ store：将Properties中的键值对存储到配置文件中，在IDEA中，保存信息到配置文件，如果含有中文，会存储为unicode码。

## 2 应用实例

![](https://img-blog.csdnimg.cn/1cd14444d25c438081e9d9878ff16d9d.png?x-oss-
process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aWI5pav5p2O5YWI55Sf,size_17,color_FFFFFF,t_70,g_se,x_16)

###  （1）传统方法

在src目录下创建mysql.properties配置文件，里面的内容：

![](https://img-blog.csdnimg.cn/5093f1881818428a96a1468d35f6ea03.png?x-oss-
process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aWI5pav5p2O5YWI55Sf,size_11,color_FFFFFF,t_70,g_se,x_16)

    
    
    public class Properties01 {
        public static void main(String[] args) throws IOException {
    
    
            //读取mysql.properties 文件，并得到ip, user 和 pwd
            BufferedReader br = new BufferedReader(new FileReader("src\\mysql.properties"));
            String line = "";
            while ((line = br.readLine()) != null) { //循环读取
                String[] split = line.split("=");
                //如果我们要求指定的ip值
                if("ip".equals(split[0])) {
                    System.out.println(split[0] + "值是: " + split[1]);
                }
            }
    
            br.close();
        }
    }
    

### （2）properties类方法

    
    
    public class Properties02 {
        public static void main(String[] args) throws IOException {
            //使用Properties 类来读取mysql.properties 文件
    
            //1. 创建Properties 对象
            Properties properties = new Properties();
            //2. 加载指定配置文件
            properties.load(new FileReader("src\\mysql.properties"));
            //3. 把k-v显示控制台
            properties.list(System.out);
            //4. 根据key 获取对应的值
            String user = properties.getProperty("user");
            String pwd = properties.getProperty("pwd");
            System.out.println("用户名=" + user);
            System.out.println("密码是=" + pwd);
    
    
    
        }
    }
    
    
    public class Properties03 {
        public static void main(String[] args) throws IOException {
            //使用Properties 类来创建 配置文件, 修改配置文件内容
    
            Properties properties = new Properties();
            //创建
            //1.如果该文件没有key 就是创建
            //2.如果该文件有key ,就是修改
            /*
                Properties 父类是 Hashtable ， 底层就是Hashtable 核心方法
                public synchronized V put(K key, V value) {
                    // Make sure the value is not null
                    if (value == null) {
                        throw new NullPointerException();
                    }
    
                    // Makes sure the key is not already in the hashtable.
                    Entry tab[] = table;
                    int hash = key.hashCode();
                    int index = (hash & 0x7FFFFFFF) % tab.length;
                    @SuppressWarnings("unchecked")
                    Entry entry = (Entry)tab[index];
                    for(; entry != null ; entry = entry.next) {
                        if ((entry.hash == hash) && entry.key.equals(key)) {
                            V old = entry.value;
                            entry.value = value;//如果key 存在，就替换
                            return old;
                        }
                    }
    
                    addEntry(hash, key, value, index);//如果是新k, 就addEntry
                    return null;
                }
    
             */
            properties.setProperty("charset", "utf8");
            properties.setProperty("user", "汤姆");//注意保存时，是中文的 unicode码值
            properties.setProperty("pwd", "888888");
    
            //将k-v 存储文件中即可
            //注意null是指properties配置文件没有要说明的注释，如果有的话会在配置文件的
            //最上方显示。
            properties.store(new FileOutputStream("src\\mysql2.properties"), null);
            System.out.println("保存配置文件成功~");
    
        }
    }

