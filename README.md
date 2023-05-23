# Snake

Игрок управляет змейкой, которая перемещается по игровому полю. Змейка любит кушать яблоки, которые появляются на игровом поле. В самом начале игры змейка состоит всего из одного элемента. Но как только змейка съедает яблоко, её тело вырастает, и она состоит уже из двух элементов. По мере игры змейка может вырастать до внушительных размеров, что требует от игрока умелого управления. За каждое съеденное яблоко игрок получает очко. Чем больше очков набирает игрок, тем лучше. Игра заканчивается когда змейка сталкивается с границей экрана или сама с собой.

## Игоровое поле

Игровое поле представляет собой прямоугольную область, состоящую из элементов (точек). `width` - ширина внутренней области поля в элементах. `height` - высота внутренней области поля в элементах. На дисплее элементы поля изображаются квадратиками размера `SCALE⨯SCALE`, где `SCALE` - масштаб.

```
   0123456789  (width = 10)
  +----------+
 0|          |
 1|          |
 2|          |
 3|          |
 4|          |
 5|   ####   |   # — тело змейки
 6|   #  #   |   + - голова змейки
 7|   #  #   |   @ - яблоко
 8|   #  +   |
 9|   #      |
10|   #      |
11|          |
12|      @   |
13|          |
14|          |
15|          |
16|          |
17|          |
18|          |
19|          |
  +----------+
(height = 20)
```

## Элемент игорового поля
Элемент игрового поля задаётся парой целых чисел `(x,y)` - координата точки внутри поля. Допустимые состояния элемента:
- пустой;
- яблоко;
- элемент змейки.

В коде игры представлен классом `Element`.

## Яблоко
Яблоко появляется на случайном элементе поля. Если голова змейки оказывается на одном элементе с яблоком, то происходит:
1. яблоко исчезает с поля;
1. змейка вырастает на 1 элемент;
1. появляется новое яблоко на случайном элементе поля (не совпадает ни с одним элементом змейки).

## Змейка
Тело змейки состоит из элементов, каждый задаётся парой координат `(x,y)`. Первый элемент по ходу движения змейки называется головой, а последний - хвостом.

### Структура данных массив ([Python list](https://docs.python.org/3/library/stdtypes.html#lists))

Можно думать о змейке как о поезде, состоящим из локомотива и вагонов. Когда голова змейки перемещается вперёд на один элемент, остальные элементы так же по очереди перемещаются вперёд. Такая операция **сдвигает** все элементы змейки. На примере ниже змейка движется справа-налево, элементы содержаться в массиве и пронумерованы от 0 до 3.

```
   0123456789    голова                хвост
  +----------+      0      1      2      3
0 |   +###   |   [(3,0), (4,0), (5,0), (6,0)]

   0123456789    голова                хвост
  +----------+      0      1      2      3
0 |  +###    |   [(2,0), (3,0), (4,0), (5,0)]
```

Что произошло с массивом после одного шага змейки:
1. значение по индексу 2 `(5,0)` скопировано в элемент по индексу 3 (теперь новый хвост, а старого `(6,0)` больше нет);
1. значение по индексу 1 `(4,0)` скопировано в элемент по индексу 2;
1. значение по индексу 0 `(3,0)` скопировано в элемент по индексу 1;
1. в элемент по индексу 0 записано новое значение `(2,0)` (новая голова).

Таким образом, один шаг змейки затрону все элементы её тела.

### Структура данных очередь ([Python deque](https://docs.python.org/3/library/collections.html#deque-objects))

Существует более оптимальный способ хранения и обработки элементов тела змейки, именно его мы и будем использовать. Будем думать о змейке как об очереди людей на базаре, где каждый человек - это элемент змейки. В голове змейки находиться самый новый элемент змейки (слева), а в хвосте - самый старый (справа). При шаге змейки происходит всего два действия:
1. новый элемент добавляется в конец очереди (слева) и становиться новой головой;
1. хвостовой элемент (крайний справа) удаляется из очереди.

```
   0123456789           голова                   хвост
  +----------+             3       2       1       0
0 |   +###   |           (3,0) - (4,0) - (5,0) - (6,0)

   0123456789    голова                  хвост
  +----------+      4      3       2       1
0 |  +###    |   (2,0) - (3,0) - (4,0) - (5,0)
```

При этом остальные элементы остаются на своих местах. Вне зависимости от длины змейки, требуется всего две операции, чтобы сделать шаг. Хотя визуальной разницы на дисплее между этими двумя подходами, игрок не увидит.

В коде игры представлен классом `Snake`.
