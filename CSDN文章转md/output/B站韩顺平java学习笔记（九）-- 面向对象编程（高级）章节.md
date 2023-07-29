**目录**

一 类变量和类方法

1 类变量

（1）定义

（2）语法

（3）访问

（4）使用注意事项和细节讨论

2 类方法

（1）基本介绍

（2）语法

（3）调用

（4）使用场景

（5）使用注意事项和细节讨论

二 理解main方法语法 static

1 解释main方法的形式：public static void main(String[] args){}

2 特别提示

3 在idea中运行main方法传入参数

三 代码块

1 基本介绍

2 基本语法

3 注意说明

4 代码块

5 使用注意事项和细节讨论

四 单例设计模式

1 介绍

2 应用实例

五 final 关键字

1 基本介绍

2 使用注意事项和细节讨论

六 抽象类

1 介绍

2 使用注意事项和细节讨论

3 最佳实践—模板设计模式

七 接口

1 基本介绍

2 语法

3 使用注意事项和使用细节

4 实现接口VS继承类

5 一道练习题

6 接口的多态特性

（1）多态参数

（2）多态数组

（3）多态存在参数传递现象

（4）练习题

八 内部类

1 基本介绍

2 基本语法

3 内部类的分类

（1）定义在外部类局部位置上

（2）定义在外部类的成员位置上

知识点

1 获取当前的时间 返回long类型数据

2 获取对象的运行类型

3 匿名内部类没有构造器

* * *

# 一 类变量和类方法

## 1 类变量

### （1）定义

类变量也叫静态变量/静态属性，是该类的所有对象共享的变量，任何一个该类的对象去访问它时，取到的都是相同的值，同样任何一个该类的对象取修改它时，修改的也是同一个变量。

### （2）语法

访问修饰符 static 数据类型 变量名；【推荐】

static 数据类型 变量名；

### （3）访问

类名.类变量名；【推荐】

或者 对象名.类变量名；【静态变量的访问修饰符的访问权限和范围 和 普通属性是一样的】

### （4）使用注意事项和细节讨论

① 什么时候需要使用类变量：

当我们需要让某个类的所有对象都共享一个变量时，就可以考虑使用类变量（静态变量）：比如：定义学生类，统计所有学生交了多少钱，Student(name,static
fee)；

② 类变量与实例变量（普通属性）区别：

类变量是该类的所有对象共享的，而实例变量是每个对象独享的；

③ 加上static称为类变量或静态变量，否则称为实例变量/普通变量/非静态变量；

④ 类变量可以通过 类名.类变量名 【推荐】或者 对象名.类变量名 来访问；【前提是 满足访问修饰符的访问权限和范围】

⑤ 实例变量不能通过 类名.类变量名 方式访问；

⑥ 类变量实在类加载时就初始化了，就是说，即使你没有创建对象，只要类加载了，就可以使用类变量了；

⑦ 类变量的生命周期是随类的加载开始，随着类消亡而销毁。

## 2 类方法

### （1）基本介绍

类方法也叫静态方法。

### （2）语法

访问修饰符 static 数据返回类型 方法名(){ }【推荐】

static 访问修饰符 数据返回类型 方法名(){ }

### （3）调用

使用方法：类名.类方法名 或者 对象名.类方法名 【前提是 满足访问修饰符的访问权限和范围】

### （4）使用场景

当方法中不涉及到任何对象相关的成员，则可以将方法设计成静态方法，提高开发效率。

### （5）使用注意事项和细节讨论

① 类方法和普通方法都是随着类的加载而加载，将结构信息存储在方法区：

类方法中无this的参数，普通方法中隐含着this的参数；

② 类方法可以通过类名调用，也可以通过对象名调用；

③ 普通方法和对象有关，需要通过对象名调用，比如对象名.方法名（参数），不能通过类名调用；

④ 类方法中不允许使用和对象有关的关键字，比如this和super。普通方法（成员方法）可以；

⑤ 类方法（静态方法）中只能访问静态变量或静态方法；

⑥ 普通成员方法既可以访问非静态成员，也可以访问静态成员。

小结：静态方法只能访问静态成员，非静态的方法可以访问静态成员和非静态成员。（必须遵守访问权限）

# 二 理解main方法语法 static

## 1 解释main方法的形式：public static void main(String[] args){}

（1）main方法是虚拟机调用；

（2）java虚拟机需要调用类的main()方法，所以该方法的访问权限必须是public；

（3）java虚拟机在执行main()方法时不必创建对象，所以该方法必须是static；

（4）该方法接受String类型的数组参数，该数组中保存执行java命令时传递给所运行的类的参数；

（5）例如：java 执行的程序 参数1 参数2 参数3

![](https://img-blog.csdnimg.cn/ebc820a9350841e8a21979235c70866f.png)

## 2 特别提示

（1）在main()方法中，我们可以直接调用main方法所在类的静态方法或者静态属性；

（2）但是，不能直接访问该类中的非静态成员，必须创建该类的一个实例对象后，才能通过这个对象去访问类中的非静态成员。

## 3 在idea中运行main方法传入参数

点![](https://img-blog.csdnimg.cn/ccb8c7c09afa421e9dfe1d21b88fe420.png)

点Edit Configurations,在Program arguments添加即可

![](https://img-blog.csdnimg.cn/708dc47353b543259d4a0e3cb8a594d1.png?x-oss-
process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5aWI5pav5p2O5YWI55Sf,size_20,color_FFFFFF,t_70,g_se,x_16)

# 三 代码块

## 1 基本介绍

代码化块又称初始化块，属于类中的成员（即 是类的一部分），类似于方法，将逻辑语句封装在方法体中，通过{}包围起来。

但和方法不同，没有方法名，没有返回，没有参数，只有方法体，而且不用通过对象或者显式调用，而是加载类时，或创建对象时隐式调用。

## 2 基本语法

[修饰符]{

代码

}；

## 3 注意说明

（1）修饰符可以选，要写的话，也只能写static；

（2）代码块分为两类，使用static修饰的叫静态代码块，没有static修饰的叫做普通代码块/非静态代码块；

（3）逻辑语句可以为任何逻辑语句（输入、输出、方法调用、循环、判断等）；

（4）；号可以写上，也可以省略。

## 4 代码块

（1）相当于另外一种形式的构造器（对构造器的补充机制），可以做初始化的操作；

（2）使用场景：如果多个构造器中都有重复的语句，可以抽取到初始化块中，提高代码重用性；

（3）不管调用哪个代码块，创建对象，都会先调用代码块的内容；

（4）代码块调用的顺序优先于构造器。

## 5 使用注意事项和细节讨论

（1）static代码块也叫静态代码块，作用就是对类进行初始化，而且它随着类的加载而执行，并且只会执行一次。（因为类只会加载一次）如果是普通代码块，每创建一个对象，就执行。

（2）类什么时候被加载

① 创建对象实例时（new）；

② 创建子类对象实例，父类也会被加载；

③ 使用类的静态成员时（静态属性，静态方法）。

④ 使用子类的静态成员时，父类也会被加载。

（3）普通的代码块，在创建对象实例时，会被隐式的调用，被创建一次，就会调用一次；如果只是使用类的静态成员时，普通的代码块不会执行。

（4）创建一个对象时，在一个类调用顺序是：🚩

① 调用静态代码块和静态属性初始化（注意：静态代码块和静态属性初始化调用的优先级一样，如果有多个静态代码块和多个静态变量初始化，则按题目定义的顺序调用）；

② 调用普通代码块和普通属性的初始化（注意：普通代码块和普通属性初始化调用的优先级一样，如果有多个普通代码块和多个普通属性初始化，则按定义顺序调用）

③ 调用构造方法。

（5）构造器 的最前面其实隐含了 super()和调用普通代码块，静态相关的代码块，属性初始化，在类加载时候，就执行完毕了，因此是优先于
构造器和普通代码块执行的。

（6）创建资格子类对象时，他们的静态代码块，静态属性初始化，普通代码块，普通属性初始化，构造方法的调用顺序如下：

① 父类的静态代码块和静态属性（优先级一样，按定义顺序执行）；

② 子类的静态代码块和静态属性（优先级一样，按定义顺序执行）；

③ 父类的普通代码块和普通属性初始化（优先级一样，按定义顺序执行）；

④ 父类的构造方法；

⑤ 子类的普通代码块和普通属性初始化（优先级一样，按定义顺序执行）；

⑥ 子类的构造方法

（7）静态代码块只能直接调用静态成员（静态属性和静态方法），普通代码块可以调用任意成员。

**注意注意：static代码块只会调用一次**

# 四 单例设计模式

## 1 介绍

单例（单个的实例）

（1）所谓类的单例设计模式，就是采取一定的方法保证在整个的软件系统中，对某个类只能存在一个对象实例，并且该类只提供一个取得其对象实例的方法。

（2）单例模式有两种方式：1）饿汉式；2）懒汉式

## 2 应用实例

（1）饿汉式：饿汉式在类加载时就创立了对象，有可能会出现只创建不适用的情况

步骤：

① 构造器私有化 =>防止直接new；

② 类的内部创建对象；

③ 向外暴露一个静态的公共方法。

    
    
    public class simpleClass {
        //1 构造器私有化
        private simpleClass(){}
        //2 类内部创建static对象
        private static simpleClass instance = new simpleClass();
        //3 向类外提供一个公共的接受对象的static方法
        public static simpleClass getInstance(){
            return instance;
        }
    }

（2）懒汉式：弥补饿汉式的缺点，什么时候创建，什么时候使用

步骤：

① 构造器私有化 =>防止直接new；

② 类的内部创建对象，但不new；

③ 向外暴露一个静态的公共方法，调用该方法时候再new，再次调用时候，会返回上一次创建的对象，保证单例。

    
    
    class Cat{
        private String name;
        public static int n1 = 99;
        private static Cat cat;//创建一个对象，未new
        // 构造器私有化
        private Cat(String name){
            this.name = name;
        }
    
        public static Cat getCat(){
            if (cat == null){
                cat = new Cat("小可爱");
            }
            return cat;
        }
    
        @Override
        public String toString() {
            return "Cat{" +
    
                    "name='" + name + '\'' +
                    '}';
        }
    }

（3）饿汉式VS懒汉式

① 二者最主要的区别在于创建对象的时机不同：饿汉式是在类加载就创建了对象实例；而懒汉式是在使用时才创建；

② 饿汉式不存在线程安全问题，懒汉式存在线程安全问题；（待完善）

③ 饿汉式存在浪费资源的可能。因为如果程序员一个对象实例都没有使用，那么饿汉式创建的对象就浪费了，懒汉式是使用时才创建，就不存在这个问题；

④ 在javaSE标准类中，java.lang.Runtime就是经典的单例模式。

# 五 final 关键字

## 1 基本介绍

final可以修饰类、属性、方法和局部变量。

在某些情况下，可能有一下需求，就会用到final：

（1）当不希望类被继承时，可以用final修饰；

（2）当不希望父类的某个方法被子类覆盖/重写（overside）时，可以用final关键字修饰；

（3）当不希望类的某个属性的值被修改，可以用final修改；

（4）当不希望某个局部变量被修改，可以用final修改。

## 2 使用注意事项和细节讨论

（1）final修饰的属性又叫常量，一般用 XX_XX_XX 来命名；

（2）final修饰的属性（不是静态时）在定义是，必须赋初值，并且以后不能再修改，赋值可以再如下位置之一【选择一个位置赋初值即可】：

① 定义时；② 在构造器中；③ 在代码块中。

    
    
    class AA{
        private final double TAX_RATE = 0.08;//定义时赋值
        private final double TAX_RATE1;
        private final double TAX_RATE2;
        
        public AA(){
            TAX_RATE1 = 1.1;//在构造器赋值
        }
        {
            TAX_RATE2 = 2.2;//在代码块中赋值
        }
    }

（3）如果final修饰的属性是静态的，则初始化的位置只能是：

① 定义时；② 在静态代码块中。不能在构造器中赋值，因为static属性在类加载时候就有了，但是构造器是在对象创建时才调用的。

（4）final类不能继承，但是可以实例化对象；

（5）如果类不是final类，但是含有final方法， 则该方法虽然不能重写，但是可以被继承；

（6）一般来说，如果一个类已经是final类了，就没有必要再将方法修饰成final方法；

（7）final不能修饰构造方法（即构造器）；

（8）final和static往往搭配使用，效率更高，底层编译器做了优化处理；

    
    
    class Demo{
        public static final int i =16;
        //public final static int i =16;也可以
        static{
            System.out.println("lyx");
        }
    }
    
    //此时调用i变量时候不会加载类Demo

（9）包装类（Integer，Double，Float，Boolean等都是final），String也是final类。

# 六 抽象类

当父类的一些方法不能确定时，可以用abstract关键字来修饰该方法，这个方法就是抽象方法，用abstract来修饰该类就是抽象类。抽象类会被继承，由其子类来实现抽象方法。

## 1 介绍

（1）用abstract关键字来修饰一个类时，这个类就叫抽象类；

访问修饰符 abstract 类名{

}

（2）用abstract关键字来修饰一个方法时，这个方法就是抽象方法；

访问修饰符 abstract 返回类型 方法名（参数列表）；//没有方法体

（3）抽象类的价值更多作用是在于设计，是设计者设计好后，让子类继承并实现抽象类（）；

## 2 使用注意事项和细节讨论

（1）抽象类不能被实例化；

（2）抽象类不一定要包括abstract方法，也就是说抽象类可以没有abstract方法，还可以有实现的方法；

（3）一旦类包含了abstract方法，则这个类必须声明为abstract；

（4）abstract只能修饰类和方法，不能修饰属性和其它的；

（5）抽象类可以有任意成员【抽象类的本质还是类】；

（6）抽象方法不能有主体；

（7）如果一个类继承了抽象类，则它必须实现抽象类的所有重抽象方法，除非它自己也声明为abstract类；

（8）抽象方法不饿能使用private、final和static来修饰，因为这些关键字都是和重写相违背的。

因为private的话，子类就不能重写该方法了；final的话，就没有子类了；static关键字与重写无关。

## 3 最佳实践—模板设计模式

    
    
    //Template类
    public abstract class Template {
        private long start;
        private long end;
    
        public void calculate(){
            start = System.currentTimeMillis();
            System.out.println(start);
            job();
            end = System.currentTimeMillis();
            System.out.println(end);
            System.out.println(end - start);
        }
        public abstract void job();
    
    }
    
    
    //AA类
    public class AA extends Template{
        @Override
        public void job() {
            int num = 0;
            for (int i = 1; i < 800000; i++) {
                num += i;
            }
        }
    
        @Override
        public void calculate() {
            super.calculate();
        }
    }

# 七 接口

## 1 基本介绍

接口就是给出一些没有实现的方法（即抽象方法，并且可以不用写abstract关键字），封装到一起，到某个类要使用的时候，再根据具体情况把这些方法写出来。

## 2 语法

interface 接口名{

//属性

//方法

}

实现接口：

class 类名 implements 接口{

自己属性；

自己方法；

必须实现的接口的抽象方法

}

**注意：** **① 在jdk7.0前 接口里的所有方法都没有方法体，即都是抽象方法；**

**② 在jdk8.0后 接口可以有静态方法，默认方法（需要default关键字修饰），也就是说接口中可以有方法的具体实现。**

## 3 使用注意事项和使用细节

（1）接口不能被实例化；

（2）接口中所有的方法是 public方法，接口中抽象方法，可以不用abstract修饰；

（3）一个普通类实现接口，就必须将该接口的所有抽象方法都实现，可以用alt+enter来解决；

（4）抽象类去实现接口时，可以不实现接口的抽象方法；

（5）一个类同时可以实现多个接口；

（6）接口中的属性，只能是final的，而且是public static final 修饰符，比如：int a = 1；实际上是public static
final int a = 1；（必须初始化）；

（7）接口中属性的访问形式：接口名.属性名；

（8）接口不饿能继承其他的类，但可以继承多个别的接口；

（9）接口的修饰符只能是public和默认，这点和类的修饰符是一样的。

## 4 实现接口VS继承类

（1）接口和继承解决的问题不同

继承的价值主要在于：解决代码的复用性和可维护性。

接口的价值主要在于：设计，设计好各种规范（方法），让其他类去实现这些方法，即更加的灵活。

（2）接口比继承更灵活

接口比继承更加灵活，继承是满足is - a的关系，而接口只需满足like - a 的关系

（3）接口在一定程度上实现了代码解耦（即：接口规范性+动态绑定机制）。

## 5 一道练习题

    
    
    public class InterfaceExercise01 {
        public static void main(String[] args) {
            B b = new B();//ok
            System.out.println(b.a);  //23
            System.out.println(A.a);  //23
            System.out.println(B.a);  //23
        }
    }
    
    interface A {
        int a = 23; //等价 public static final int a = 23;
    }
    
    class B implements A {//正确
    }

## 6 接口的多态特性

### （1）多态参数

    
    
    public class InterfacePolyParameter {
        public static void main(String[] args) {
    
            //接口的多态体现
            //接口类型的变量 if01 可以指向 实现了IF接口类的对象实例
            IF if01 = new Monster();
            if01 = new Car();
    
            //继承体现的多态
            //父类类型的变量 a 可以指向 继承AAA的子类的对象实例
            AAA a = new BBB();
            a = new CCC();
        }
    }
    
    interface IF {}
    class Monster implements IF{}
    class Car implements  IF{}
    
    class AAA {
    
    }
    class BBB extends AAA {}
    class CCC extends AAA {}

### （2）多态数组

    
    
    public class InterfacePolyArr {
        public static void main(String[] args) {
    
            //多态数组 -> 接口类型数组
            Usb[] usbs = new Usb[2];
            usbs[0] = new Phone_();
            usbs[1] = new Camera_();
            /*
            给Usb数组中，存放 Phone  和  相机对象，Phone类还有一个特有的方法call（），
            请遍历Usb数组，如果是Phone对象，除了调用Usb 接口定义的方法外，
            还需要调用Phone 特有方法 call
             */
            for(int i = 0; i < usbs.length; i++) {
                usbs[i].work();//动态绑定..
                //和前面一样，我们仍然需要进行类型的向下转型
                if(usbs[i] instanceof Phone_) {//判断他的运行类型是 Phone_
                    ((Phone_) usbs[i]).call();
                }
            }
    
        }
    }
    
    interface Usb{
        void work();
    }
    class Phone_ implements Usb {
        public void call() {
            System.out.println("手机可以打电话...");
        }
    
        @Override
        public void work() {
            System.out.println("手机工作中...");
        }
    }
    class Camera_ implements Usb {
    
        @Override
        public void work() {
            System.out.println("相机工作中...");
        }
    }
    

### （3）多态存在参数传递现象

    
    
    public class InterfacePolyPass {
        public static void main(String[] args) {
            //接口类型的变量可以指向，实现了该接口的类的对象实例
            IG ig = new Teacher();
            //如果IG 继承了 IH 接口，而Teacher 类实现了 IG接口
            //那么，实际上就相当于 Teacher 类也实现了 IH接口.
            //这就是所谓的 接口多态传递现象.
            IH ih = new Teacher();
        }
    }
    
    interface IH {
        void hi();
    }
    interface IG extends IH{ }
    class Teacher implements IG {
        @Override
        public void hi() {
        }
    }

### （4）练习题

    
    
    public class InterfaceExercise02 {
        public static void main(String[] args) {
    
        }
    }
    
    interface A {  // 1min 看看
        int x = 0;
    }  //想到 等价 public static final int x = 0;
    
    class B {
        int x = 1;
    } //普通属性
    
    class C extends B implements A {
        public void pX() {
            //System.out.println(x); //错误，原因不明确x
            //可以明确的指定x
            //访问接口的 x 就使用 A.x
            //访问父类的 x 就使用 super.x
            System.out.println(A.x + " " + super.x);
        }
    
        public static void main(String[] args) {
            new C().pX();
        }
    }

# 八 内部类

## 1 基本介绍

一个类的内部又完整的嵌套了另一个类结构。被嵌套的类称为内部类（inner class），嵌套其他类的类称为外部类（outer
class）。是我们类的第五大成员（类的五大成员：属性、方法、构造器、代码块、内部类），内部类最大的特点就是可以直接访问私有属性，并且可以体现类与类之间的包含关系。

## 2 基本语法

class Outer{ //外部类

class Inner{ //内部类

}

}

class Other{ //外部其他类

}

## 3 内部类的分类

### （1）定义在外部类局部位置上

**① 局部内部类（有类名）**

说明：局部内部类是定义在外部类的局部位置，比如方法中，并且有类名。

a 可以直接访问外部类的所有成员，包括私有的；

b 不能添加访问修饰符，因为它的地位就是一个局部变量，局部变量是不能使用修饰符的。但是可以使用final修饰，因为局部变量也可以使用final；

c 作用域：仅仅在定义它的方法或者代码块中；

d 局部内部类---访问---外部类成员【访问方式：直接访问】

e 外部类---访问---
局部内部类的成员【访问方式：创建对象（外部类[在main方法创建]和局部内部类[在写有局部内部类的外部类方法中创建按]都要创建），再访问（注意：必须在作用域中）】。

注意：局部内部类定义在方法/代码块中；作用域在方法体或者代码块中；本质仍然是一个类。

f 外部其他类---不能访问---->局部内部类（因为 局部内部类地位是一个局部变量）

g
如果外部类和局部内部类的成员重名时，默认遵循就近原则，如果想访问外部类的成员，则可以使用（外部类名.this.成员）//其中外部类名.this表示调用局部内部类方法的外部类的对象。

**② 匿名内部类（没有类名🚩）**

（1）本质是类（2）内部类（3）该类没有名字（4）同时还是一个对象

说明：匿名内部类是定义在外部类的局部位置，比如方法中，并且没有类名

a 基本语法

new 类或接口（参数列表）{

类体

}；

    
    
    public class AnonymousInnerClass {
        public static void main(String[] args) {
            Outer04 outer04 = new Outer04();
            outer04.method();
        }
    }
    
    class Outer04 { //外部类
        private int n1 = 10;//属性
        public void method() {//方法
            //基于接口的匿名内部类🚩
            //老韩解读
            //1.需求： 想使用IA接口,并创建对象
            //2.传统方式，是写一个类，实现该接口，并创建对象
            //3.老韩需求是 Tiger/Dog 类只是使用一次，后面再不使用
            //4. 可以使用匿名内部类来简化开发
            //5. tiger的编译类型 ? IA
            //6. tiger的运行类型 ? 就是匿名内部类  Outer04$1
            /*
                我们看底层 会分配 类名 Outer04$1
                class Outer04$1 implements IA {
                    @Override
                    public void cry() {
                        System.out.println("老虎叫唤...");
                    }
                }
             */
            //7. jdk底层在创建匿名内部类 Outer04$1,立即马上就创建了 Outer04$1实例，并且把地址
            //   返回给 tiger
            //8. 匿名内部类使用一次，就不能再使用
            IA tiger = new IA() {
                @Override
                public void cry() {
                    System.out.println("老虎叫唤...");
                }
            };
            System.out.println("tiger的运行类型=" + tiger.getClass());
            tiger.cry();
            tiger.cry();
            tiger.cry();
    
        }
    }
    interface tiger{
        public void cry();
    }
    
    
    public class AnonymousInnerClass {
        public static void main(String[] args) {
            Outer04 outer04 = new Outer04();
            outer04.method();
        }
    }
    
    class Outer04 { //外部类
        private int n1 = 10;//属性
        public void method() {//方法
            
            //演示基于类的匿名内部类🚩
            //分析
            //1. father编译类型 Father
            //2. father运行类型 Outer04$2
            //3. 底层会创建匿名内部类
            /*
                class Outer04$2 extends Father{
                    @Override
                    public void test() {
                        System.out.println("匿名内部类重写了test方法");
                    }
                }
             */
            //4. 同时也直接返回了 匿名内部类 Outer04$2的对象
            //5. 注意("jack") 参数列表会传递给 构造器
            Father father = new Father("jack"){
    
                @Override
                public void test() {//可以不重写
                    System.out.println("匿名内部类重写了test方法");
                }
            };
            System.out.println("father对象的运行类型=" + father.getClass());//Outer04$2
            father.test();
    
            //基于抽象类的匿名内部类🚩
            Animal animal = new Animal(){
                @Override
                void eat() {//必须是实现，因为是抽象类
                    System.out.println("小狗吃骨头...");
                }
            };
            animal.eat();
        }
    }
    
    class Father {//类
        public Father(String name) {//构造器
            System.out.println("接收到name=" + name);
        }
        public void test() {//方法
        }
    }
    
    abstract class Animal { //抽象类
        abstract void eat();
    }
    

b 匿名内部类的语法比较奇特，因为匿名内部类即是一个类的定义，同时它本身也是一个对象，因此从语法上来看，它既有定义类的特征，也有创建对象的特征；

c 可以直接访问外部类的所有成员，包含私有的；

d 不能添加访问修饰符，因为它的地位是一个局部变量；

e 作用域：仅仅在定义它的方法或代码块中；

f 匿名内部类---访问--->外部类成员【访问方式：直接访问】

g 外部其他类---不能访问--->匿名内部类【因为匿名内部类地位就是一个局部变量】

h 如果外部类和匿名内部类的成员重名时，匿名内部类访问的话，默认遵循就近原则，如果想访问外部类的成员，则可以使用（外部类名.this.成员）去访问。

    
    
    public class AnnonyInnerClass {
        public static void main(String[] args) {
            AAA aaa = new AAA();
            aaa.hi();
        }
    }
    class AAA{
        public int i = 1;
        public void hi(){
            Person p = new Person(){
                public int  i = 2;
                @Override
                public void say() {
                    System.out.println("say");
                }
            };
            p.say();
            //直接调用，可以传实参🚩
            new Person(){
                @Override
                public void speak(String str) {
                    super.speak(str);
                }
            }.speak("haha");
        }
    }
    class Person{
        public void say(){
        }
        public void speak(String str){
            System.out.println("speak:" + str);
        }
    }

**③ 匿名内部类的实践**

Ⅰ _当作实参直接传递，简洁高效_

    
    
    public class InnerClassExercise01 {
        public static void main(String[] args) {
    
            //当做实参直接传递，简洁高效
            f1(new IL() {
                @Override
                public void show() {
                    System.out.println("这是一副名画~~...");
                }
            });
            //传统方法
            f1(new Picture());
    
        }
    
        //静态方法,形参是接口类型
        public static void f1(IL il) {
            il.show();
        }
    }
    //接口
    interface IL {
        void show();
    }
    //类->实现IL => 编程领域 (硬编码)
    class Picture implements IL {
    
        @Override
        public void show() {
            System.out.println("这是一副名画XX...");
        }
    }

Ⅱ _课堂练习_

    
    
    public class InnerClassExercise01 {
        public static void main(String[] args) {
            CellPhone cellPhone = new CellPhone();
            cellPhone.alarmclock(new Bell() {
                @Override
                public void ring() {
                    System.out.println("懒猪起床了");
                }
            });
            cellPhone.alarmclock(new Bell() {
                @Override
                public void ring() {
                    System.out.println("小伙伴上课了");
                }
            });
        }
    }
    interface Bell{
        void ring();
    }
    class CellPhone{
        public void alarmclock(Bell bell){
            bell.ring();
        }
    }

### （2）定义在外部类的成员位置上

**① 成员内部类（没有static修饰）**

说明：成员内部类是定义在外部类的成员位置，并且没有static修饰。

a 可以直接访问外部类的所有成员，包括私有的

b 可以添加任意访问修饰符（public、protected、默认、private），因为它的地位就是一个成员。

c 作用域，和外部类的其他成员一样，为整个类体。

d 成员内部类---访问--->外部类成员（比如：属性）【访问方式：直接访问】

e 外部类---访问--->成员内部类【访问方式：创建对象，再访问】

f 外部其他类---访问--->成员内部类

    
    
    public class MemberInnerClass01 {
        public static void main(String[] args) {
            Outer08 outer08 = new Outer08();
            outer08.t1();
    
            //外部其他类，使用成员内部类的三种方式
            //老韩解读
            // 第一种方式🚩
            // outer08.new Inner08(); 相当于把 new Inner08()当做是outer08成员
            // 这就是一个语法，不要特别的纠结.
            Outer08.Inner08 inner08 = outer08.new Inner08();
            inner08.say();
            // 第二种方式🚩 在外部类中，编写一个方法，可以返回 Inner08对象
            Outer08.Inner08 inner08Instance = outer08.getInner08Instance();
            inner08Instance.say();
    
    
        }
    }
    
    class Outer08 { //外部类
        private int n1 = 10;
        public String name = "张三";
    
        private void hi() {
            System.out.println("hi()方法...");
        }
    
        //1.注意: 成员内部类，是定义在外部内的成员位置上
        //2.可以添加任意访问修饰符(public、protected 、默认、private),因为它的地位就是一个成员
        public class Inner08 {//成员内部类
            private double sal = 99.8;
            private int n1 = 66;
            public void say() {
                //可以直接访问外部类的所有成员，包含私有的
                //如果成员内部类的成员和外部类的成员重名，会遵守就近原则.
                //，可以通过  外部类名.this.属性 来访问外部类的成员
                System.out.println("n1 = " + n1 + " name = " + name + " 外部类的n1=" + Outer08.this.n1);
                hi();
            }
        }
        //方法，返回一个Inner08实例
        public Inner08 getInner08Instance(){
            return new Inner08();
        }
    
    
        //写方法
        public void t1() {
            //使用成员内部类
            //创建成员内部类的对象，然后使用相关的方法
            Inner08 inner08 = new Inner08();
            inner08.say();
            System.out.println(inner08.sal);
        }
    }
    

g 如果外部类和内部类的成员重名时，内部类访问的话，默认遵循就近原则，如果想访问外部类的成员，则可以使用（外部类名.this.成员）去访问。

**② 静态内部类（使用static修饰）**

说明：静态内部类是定义在外部类的成员位置，并且又static修饰。

a 可以直接访问外部类的所有静态成员，包括私有的，但不能直接访问非静态成员；

b 可以添加任意访问修饰符（public、protected、默认、private），因为它的地位就是一个成员；

c 作用域：同其他的成员，为整个类体；

d 静态内部类---访问--->外部类（比如：静态属性）【访问方式：直接访问所有静态成员】；

e 外部类---访问--->静态内部类【访问方式：创建对象，再访问】

f 外部其他类---访问--->静态内部类

g 如果外部类和静态内部类的成员重名时，静态内部类访问的时候，默认遵循就近原则，如果想访问外部类的成员，则可以使用（外部类名.成员）去访问。

    
    
    public class StaticInnerClass01 {
        public static void main(String[] args) {
            Outer10 outer10 = new Outer10();
            outer10.m1();
    
            //外部其他类 使用静态内部类
            //方式1🚩
            //因为静态内部类，是可以通过类名直接访问(前提是满足访问权限)
            Outer10.Inner10 inner10 = new Outer10.Inner10();
            inner10.say();
            //方式2🚩
            //编写一个方法，可以返回静态内部类的对象实例.
            Outer10.Inner10 inner101 = outer10.getInner10();
            System.out.println("============");
            inner101.say();
            //此地方getInner10_()为静态方法，无需创建对象（指的是outer10对象），可直接访问	
            Outer10.Inner10 inner10_ = Outer10.getInner10_();
            System.out.println("************");
            inner10_.say();
        }
    }
    
    class Outer10 { //外部类
        private int n1 = 10;
        private static String name = "张三";
        private static void cry() {}
        //Inner10就是静态内部类
        //1. 放在外部类的成员位置
        //2. 使用static 修饰
        //3. 可以直接访问外部类的所有静态成员，包含私有的，但不能直接访问非静态成员
        //4. 可以添加任意访问修饰符(public、protected 、默认、private),因为它的地位就是一个成员
        //5. 作用域 ：同其他的成员，为整个类体
        static class Inner10 {
            private static String name = "韩顺平教育";
            public void say() {
                //如果外部类和静态内部类的成员重名时，静态内部类访问的时，
                //默认遵循就近原则，如果想访问外部类的成员，则可以使用 （外部类名.成员）
                System.out.println(name + " 外部类name= " + Outer10.name);
                cry();
            }
        }
        public void m1() { //外部类---访问------>静态内部类 访问方式：创建对象，再访问
            Inner10 inner10 = new Inner10();
            inner10.say();
        }
    
        public Inner10 getInner10() {
            return new Inner10();
        }

# 知识点

## 1 获取当前的时间 返回long类型数据

System.currentTimeMillis();

## 2 获取对象的运行类型

对象名.getClass();

## 3 匿名内部类没有构造器

因为匿名内部类没有名字这个特殊性质，所以我们无从给它指定构造方法，构造方法必须和类名同名，类名都没有，构造方法就无从谈起了。但是匿名内部类可以通过直接调用父类的构造方法实现初始化。

