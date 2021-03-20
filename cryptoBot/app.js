const { Telegraf } = require("telegraf");
const bot = new Telegraf("1646391008:AAF8yoI5aXoV10BJuy9jKFC38XMm5WQd1C8");
const axios = require("axios");

bot.command("test", (ctx) => {
  bot.telegram.sendMessage(ctx.chat.id, "Jual Beli Telegram Internal", {
    reply_markup: {
      inline_keyboard: [
        [
          { text: "Lihat list toko", callback_data: "toko" },
          //   { text: "Lihat list daging", callback_data: "daging" },
        ],
        [{ text: "Lihat list pemilik", callback_data: "pemilik" }],
      ],
    },
  });
});

bot.action("toko", (ctx) => {
  ctx.deleteMessage();
  bot.telegram.sendMessage(
    ctx.chat.id,
    "List Toko: \n1.Ngene Shop\n2.Pulsa Mahasiswa",
    {
      reply_markup: {
        inline_keyboard: [
          [{ text: "Kembali ke menu utama", callback_data: "menu" }],
        ],
      },
    }
  );
});

bot.action("pemilik", (ctx) => {
  ctx.deleteMessage();
  bot.telegram.sendMessage(ctx.chat.id, "List Penjual: \n1.Haufal\n2.Maulana", {
    reply_markup: {
      inline_keyboard: [
        [{ text: "Kembali ke menu utama", callback_data: "menu" }],
      ],
    },
  });
});

bot.action("menu", (ctx) => {
  ctx.deleteMessage();
  bot.telegram.sendMessage(ctx.chat.id, "Jual Beli Telegram Internal", {
    reply_markup: {
      inline_keyboard: [
        [{ text: "Lihat list toko", callback_data: "toko" }],
        [{ text: "Lihat list pemilik", callback_data: "pemilik" }],
      ],
    },
  });
});

bot.launch();
