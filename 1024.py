"""
Demonstrates a Rich "application" using the Layout and Live classes.

"""

from datetime import datetime

from rich import box
from rich.align import Align
from rich.console import Console, Group
from rich.layout import Layout
from rich.panel import Panel
from rich.progress import BarColumn, Progress, SpinnerColumn, TextColumn
from rich.syntax import Syntax
from rich.table import Table

console = Console()


def make_layout() -> Layout:
    """Define the layout."""
    layout = Layout(name="root")

    layout.split(
        Layout(name="header", size=3),
        Layout(name="main", ratio=1),
        Layout(name="footer", size=7),
    )
    layout["main"].split_row(
        Layout(name="side"),
        Layout(name="body", ratio=2, minimum_size=60),
    )
    layout["side"].split(Layout(name="box1", size =14), Layout(name="box2", ratio=1))
    return layout


def make_main_panel(color) -> Panel:
    """Some example content."""
    main_message = Table.grid(padding=1)
    main_message.add_column(style=color)
    main_message.add_row(
        """
     _                    _                   _              _           
    / /\\                / /\\                /\\ \\         _  /\\ \\         
   / /  \\              / /  \\              /  \\ \\       /\\_\\\\ \\ \\        
  /_/ /\\ \\            / / /\\ \\            / /\\ \\ \\     / / / \\ \\ \\       
  \\_\\/\\ \\ \\          / / /\\ \\ \\           \\/_/\\ \\ \\   / / /   \\ \\ \\      
       \\ \\ \\        /_/ /  \\ \\ \\              / / /   \\ \\ \\____\\ \\ \\     
        \\ \\ \\       \\ \\ \\   \\ \\ \\            / / /     \\ \\________\\ \\    
         \\ \\ \\       \\ \\ \\   \\ \\ \\          / / /  _    \\/________/\\ \\   
        __\\ \\ \\___    \\ \\ \\___\\ \\ \\   _    / / /_/\\_\\             \\ \\ \\  
       /___\\_\\/__/\\    \\ \\/____\\ \\ \\ /\\_\\ / /_____/ /              \\ \\_\\ 
       \\_________\\/     \\_________\\/ \\/_/ \\________/                \\/_/ 
"""
    )

    time_message = Table.grid(padding=1)
    time_message.add_column(style="blue", justify="center")
    time_message.add_row(
        datetime.now().ctime().replace(":", "[blink]:[/]")
    )
    time_message.add_row(
        "[white]指针重叠时空的纷扰，还有谁回望青葱年少"
    )
    time_message.add_row(
        ""
    )
    time_message.add_row(
        "[green]项目仓库 [white] : [blue][u blue link=]还没上传~"
    )
    time_message.add_row(
        "[green]博客 [white]: [blue][u blue link=https://cx330_502.github.io]52Hz的鲸歌"
    )

    message = Table.grid(padding=1)
    message.add_column()
    message.add_column(no_wrap=True)
    message.add_row(main_message)
    message.add_row(time_message)

    message_panel = Panel(
        Align.center(
            Group("\n", Align.center(main_message),
                  "\n\n", Align.center(time_message)),
            vertical="middle",
        ),
        box=box.ROUNDED,
        padding=(1, 2),
        title="啊吧啊吧",
        border_style="bright_blue",
    )
    return message_panel

def make_pic_panel( ) -> Panel:
    main_pic = Table.grid()
    main_pic.add_column(style="blue", justify="left")
    main_pic.add_row(
        """
     __________________________________________________
    /    _________________________________________     \\
    |   |                                         |    |
    |   |  [green]C:\\> [white]python [yellow]1024.py[blue]                    |    |
    |   |  [red][b]ERROR:[/b][white] File "C:\\1024.py", line 1, ...[blue]  |    |
    |   |  [red][b]ERROR:[/b][white] File "C:\\1024.py", line 2, ...[blue]  |    |
    |   |  [red][b]ERROR:[/b][white] File "C:\\1024.py", line 3, ...[blue]  |    |
    |   |  [red][b]ERROR:[/b][white] File "C:\\1024.py", line 4, ...[blue]  |    |
    |   |  [red][b]ERROR:[/b][white] File "C:\\1024.py", line 5, ...[blue]  |    |
    |   |_________________________________________|    |
    \\__________________________________________________/
          \\___________________________________/
        ___________________________________________
     _-'    .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_
  _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_
:---------------------------------------------------------:
`---._.---------------------------------------------._.---'
        """
    )
    pic_panel = Panel(
        Align.center(
            Group(Align.center(main_pic)),
            vertical="middle",
        ),
        box=box.ROUNDED,
        padding=(1, 2),
        title="捏麻麻的",
        border_style="bright_blue",
    )
    return pic_panel
    

class Header:
    """Display header with clock."""

    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="center", ratio=1)
        grid.add_row(
            "[b]1024程序员节快乐！"
        )
        return Panel(grid, style="white on blue")


def make_syntax() -> Syntax:
    code = """\
井include 《stdio。h》

class O{
public:
    static void o(){
        std::cout << "尊嘟假嘟O.o?" <<std::endl;
    }
};
int main(){
    O.o();
    remake 0;
}    
    """
    syntax = Syntax(code, "python", line_numbers=True)
    return syntax


left_progress = Progress(
    "{task.description}",
    SpinnerColumn(),
    BarColumn(),
    TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
)
left_progress.add_task("[green]编译", total=10000)
left_progress.add_task("[magenta]计网", total=8000)
left_progress.add_task("[cyan]软分", total=6000)
right_progress = Progress(
    "{task.description}",
    SpinnerColumn(),
    BarColumn(),
    TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
)
right_progress.add_task("[yellow]网存", total=4000)
right_progress.add_task("[white]数电", total=2000)
right_progress.add_task("[purple]智能计算", total=1000)

total = sum(task.total for task in left_progress.tasks) + sum(task.total for task in right_progress.tasks)
overall_progress = Progress()
overall_task = overall_progress.add_task("All Jobs", total=int(total))

progress_table = Table.grid(expand=True)
progress_table.add_row(
    Panel(
        overall_progress,
        title="Overall Progress",
        border_style="green",
        padding=(2, 2),
    ),
    Panel(left_progress, title="[b]核心专业", border_style="red", padding=(1, 2)),
    Panel(right_progress, title="[b]一般专业", border_style="red", padding=(1, 2)),
)

colors = ["red", "green", "blue", "yellow", "magenta", "cyan", "white",  "purple"]
color_index = 0
layout = make_layout()
layout["header"].update(Header())
layout["body"].update(make_main_panel(colors[color_index]))
# layout["box2"].update(Panel(make_syntax(), border_style="green"))
# layout["box1"].update(Panel(layout.tree, border_style="red"))
layout["box2"].update(make_pic_panel())
layout["box1"].update(Panel(make_syntax(), border_style="green", title="尊嘟假嘟O.o?"))
layout["footer"].update(progress_table)

from time import sleep

from rich.live import Live

with Live(layout, refresh_per_second=10, screen=True):
    while not overall_progress.finished:
        color_index = (color_index + 0.2)
        layout["body"].update(make_main_panel(colors[int(color_index) % len(colors)]))
        if color_index > len(colors):
            color_index = 0
        sleep(0.1)
        for job in left_progress.tasks:
            if not job.finished:
                left_progress.advance(job.id)
        for job in right_progress.tasks:
            if not job.finished:
                right_progress.advance(job.id)

        completed = sum(task.completed for task in left_progress.tasks)
        completed += sum(task.completed for task in right_progress.tasks)
        overall_progress.update(overall_task, completed=completed)
