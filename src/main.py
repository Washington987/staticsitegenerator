from textnode import TextType, TextNode


def main() -> None:
    text_node_test = TextNode("This is some text for testing", TextType("link"), "https://orteil.dashnet.org/cookieclicker/")
    print(text_node_test)

main()
