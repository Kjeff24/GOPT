class Chatbox {
    constructor() {
      this.args = {
        // openButton: document.querySelector(".chatbox__button"),
        chatBox: document.querySelector(".chatbox__support"),
        sendButton: document.querySelector(".send__button"),
      };
      this.state = false;
      this.messages = [];
    }
  
    display() {
      const { sendButton, chatBox } = this.args;
  
      // openButton.addEventListener("click", () => this.toggleState(chatBox));
      sendButton.addEventListener("click", () => this.onSendButton(chatBox));
  
      // const node = chatBox.querySelector("textarea");
      // node.addEventListener("keyup", ({ key }) => {
      //   if (key === "Enter") {
      //     this.onSendButton(chatBox);
      //   }
      // });

      const node = chatBox.querySelector("textarea");
      node.addEventListener("keydown", (event) => {
        if (event.key === "Enter" && !event.shiftKey) {
          event.preventDefault(); // Prevent the default Enter behavior (submitting form)
          this.onSendButton(chatBox);
        }
      });
    }
  
    // toggleState(chatbox) {
    //   this.state = !this.state;
  
    //   if (this.state) {
    //     chatbox.classList.add("chatbox--active");
    //   } else {
    //     chatbox.classList.remove("chatbox--active");
    //   }
    // }
  
    onSendButton(chatbox) {
      var textField = chatbox.querySelector("textarea");
      let text1 = textField.value;
      if (text1 === "") {
        return;
      }
  
      let msg1 = { name: "User", message: text1 };
      this.messages.push(msg1);
      fetch(`${window.location.href}chatbot-msg/`, {
        method: "POST",
        body: JSON.stringify({ message: text1 }),
        mode: "cors",
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((r) => r.json())
        .then((r) => {
          let msg2 = { name: "Sam", message: r.answer };
          this.messages.push(msg2);
          this.updateChatText(chatbox);
          textField.value = "";
        }).catch((error) => {
          console.log("Error: ", error);
          this.updateChatText(chatbox);
          textField.value = "";
        });
    }
  
    updateChatText(chatbox) {
      var html = "";
      this.messages.slice().reverse().forEach(function (item, index) {
          if (item.name == "Sam") {
            html += `<div class="messages__item messages__item--visitor">${item.message}</div>`;
          } else {
            html += `<div class="messages__item messages__item--operator">${item.message}</div>`;
          }
        });
      const chatmessage = chatbox.querySelector(".chatbox__messages");
      chatmessage.innerHTML = html;
    }
  }
  
  const chatbox = new Chatbox();
  chatbox.display()
  