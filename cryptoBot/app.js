const { Telegraf } = require("telegraf");
const bot = new Telegraf("1646391008:AAF8yoI5aXoV10BJuy9jKFC38XMm5WQd1C8");
const axios = require("axios");

const apikey =
  "4b62382057d830c77f5dcef7a8cfe5dd25325dda1923947401ade5ddff4f8566";

function sendStartMessage(ctx) {
  let startMessage =
    "Selamat datang, bot ini memberikan informasi mengenai crypto currency";
  bot.telegram.sendMessage(ctx.chat.id, startMessage, {
    reply_markup: {
      inline_keyboard: [
        [
          { text: "Harga Crypto", callback_data: "price" },
          { text: "Coin Market Cap", url: "https://www.cryptocompare.com/" },
        ],
        [{ text: "Bot info", callback_data: "info" }],
      ],
    },
  });
}

bot.command("start", (ctx) => {
  sendStartMessage(ctx);
});

bot.action("start", (ctx) => {
  ctx.deleteMessage();
  sendStartMessage(ctx);
});

bot.action("price", (ctx) => {
  let priceMessage =
    "Dapatkan informasi harga, pilih salah satu mata uang crypto dibawah ini";
  ctx.deleteMessage();
  bot.telegram.sendMessage(ctx.chat.id, priceMessage, {
    reply_markup: {
      inline_keyboard: [
        [
          { text: "BTC", callback_data: "price-BTC" },
          { text: "ETH", callback_data: "price-ETH" },
        ],
        [
          { text: "LTC", callback_data: "price-LTC" },
          { text: "BTT", callback_data: "price-BTT" },
        ],
        [{ text: "Kembali ke menu", callback_data: "start" }],
      ],
    },
  });
});

let priceActionList = ["price-BTC", "price-ETH", "price-LTC", "price-BTT"];
bot.action(priceActionList, async (ctx) => {
  //   console.log(ctx.match.input);
  let symbol = ctx.match.input.split("-")[1];
  //   console.log(symbol);
  try {
    let res = await axios.get(
      `https://min-api.cryptocompare.com/data/pricemultifull?fsyms=${symbol}&tsyms=IDR&api_key=${apikey}`
    );
    let data = res.data.DISPLAY[symbol].IDR;

    let message = `

        Symbol: ${symbol}
        Price: ${data.PRICE}
        Open: ${data.OPENDAY}
        High: ${data.HIGHDAY}
        Low: ${data.LOWDAY}
        Supply: ${data.SUPPLY}
        Market Cap: ${data.MKTCAP}

        `;

    ctx.deleteMessage();
    bot.telegram.sendMessage(ctx.chat.id, message, {
      reply_markup: {
        inline_keyboard: [
          [
            //
            { text: "Kembali ke Harga", callback_data: "price" },
          ],
        ],
      },
    });
  } catch (err) {
    console.log(err);
    ctx.reply("Terdapat error");
  }
});

bot.action("info", (ctx) => {
  ctx.answerCbQuery();
  bot.telegram.sendMessage(ctx.chat.id, "Bot Info", {
    reply_markup: {
      keyboard: [
        [{ text: "Credits" }, { text: "API" }],
        [{ text: "Hilangkan Keyboard" }],
      ],
      resize_keyboard: true,
    },
  });
});

bot.hears("Credits", (ctx) => {
  ctx.reply("Bot ini dibuat oleh Handhika YP - Projek dengan Zal");
});

bot.hears("API", (ctx) => {
  ctx.reply("BOT ini menggunakan cryptocompare API");
});

bot.hears("Hilangkan Keyboard", (ctx) => {
  bot.telegram.sendMessage(ctx.chat.id, "Keyboard dihilangkan", {
    reply_markup: {
      remove_keyboard: true,
    },
  });
});

bot.launch();
