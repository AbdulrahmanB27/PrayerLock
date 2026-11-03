(() => {
  "use strict";
  const motionQuery = window.matchMedia("(prefers-reduced-motion: reduce)");
  const motionToggle = document.querySelector(".motion-toggle");
  const stage = document.querySelector(".sky-stage");
  const skyImage = document.querySelector("#sky-image");
  const film = document.querySelector("#product-film");
  const arabic = document.documentElement.lang === "ar";
  const skyTemplate = skyImage?.getAttribute("src").replace(
    /home-(fajr|dhuhr|asr|maghrib|isha)\.png/,
    "home-{prayer}.png",
  );
  const skies = arabic ? {
    fajr: {
      period: "سكينة ما قبل الفجر",
      line: "بداية جديدة.<br> ومساحة للصلاة.",
      description: "بنفسجي ما قبل الفجر",
    },
    dhuhr: {
      period: "وقفة في منتصف النهار",
      line: "خذ نفسًا.<br> وعد إلى اللحظة.",
      description: "زرقة الظهيرة الصافية",
    },
    asr: {
      period: "لحظة وصل في العصر",
      line: "تمهّل قليلًا.<br> واستعد سكينتك.",
      description: "ألوان العصر الدافئة",
    },
    maghrib: {
      period: "حين تغيب الشمس",
      line: "دع يومك يهدأ.<br> وأفسح وقتًا للصلاة.",
      description: "ألوان الغروب الوردية",
    },
    isha: {
      period: "ختام يسوده الهدوء",
      line: "ابتعد عن الضجيج.<br> واختم يومك بنيّة.",
      description: "زرقة الليل العميقة",
    },
  } : {
    fajr: {
      period: "The quiet before dawn",
      line: "Begin again.<br> Make space for prayer.",
      description: "Pre-dawn violet",
    },
    dhuhr: {
      period: "The midday pause",
      line: "Take a breath.<br> Return to the moment.",
      description: "Clear midday blue",
    },
    asr: {
      period: "An afternoon to reconnect",
      line: "Step away.<br> Find a little stillness.",
      description: "Warm afternoon slate",
    },
    maghrib: {
      period: "As the sun slips away",
      line: "Let the day settle.<br> Make room for prayer.",
      description: "Rose sunset",
    },
    isha: {
      period: "A peaceful close",
      line: "Leave the noise behind.<br> End your day with intention.",
      description: "Deep night indigo",
    },
  };
  let paused = motionQuery.matches;

  function updateMotion() {
    document.body.classList.toggle("motion-paused", paused);
    document.documentElement.classList.toggle("motion-paused", paused);
    if (motionToggle) {
      motionToggle.hidden = motionQuery.matches;
      motionToggle.setAttribute("aria-pressed", String(paused));
      motionToggle.querySelector(".motion-label").textContent = paused
        ? (arabic ? "استئناف الحركة" : "Resume motion")
        : (arabic ? "إيقاف الحركة" : "Pause motion");
      motionToggle.querySelector(".motion-symbol").textContent = paused
        ? "▷"
        : "Ⅱ";
    }
    if (paused && film) film.pause();
    document.querySelectorAll("[data-motion-gif]").forEach((image) => {
      image.src = paused ? image.dataset.still : image.dataset.motionGif;
      if (image.dataset.motionAlt) {
        image.alt = paused ? image.dataset.stillAlt : image.dataset.motionAlt;
      }
    });
  }

  document.body.classList.add("motion-ready");
  motionToggle?.addEventListener("click", () => {
    paused = !paused;
    updateMotion();
  });
  motionQuery.addEventListener("change", (event) => {
    paused = event.matches;
    updateMotion();
  });
  updateMotion();

  document.querySelectorAll("[data-prayer]").forEach((button) => {
    button.addEventListener("click", () => {
      const prayer = button.dataset.prayer;
      const sky = skies[prayer];
      if (!sky || !stage || !skyImage) return;
      stage.dataset.sky = prayer;
      skyImage.src = skyTemplate.replace("{prayer}", prayer);
      skyImage.alt = arabic
        ? `شاشة ${button.textContent.trim()} في تطبيق PrayerLock على أندرويد`
        : `PrayerLock ${button.textContent.trim()} Android screen`;
      document.querySelector(".sky-period").textContent = sky.period;
      document.querySelector(".sky-line").innerHTML = sky.line;
      document.querySelector("#sky-announcement").textContent =
        arabic
          ? `${button.textContent.trim()}. ${sky.description}. مواقيت الصلاة المعروضة أمثلة توضيحية.`
          : `${button.textContent.trim()}. ${sky.description}. Example prayer times.`;
      document
        .querySelectorAll("[data-prayer]")
        .forEach((item) =>
          item.setAttribute("aria-pressed", String(item === button)),
        );
    });
  });

  document.querySelectorAll(".film-trigger").forEach((link) => {
    link.addEventListener("click", () => {
      if (!film) return;
      film.focus({ preventScroll: true });
      // A visitor's explicit play action is the only trigger for video playback.
      film.play().catch(() => {
        /* Native video controls remain available. */
      });
    });
  });
  document.querySelectorAll("[data-year]").forEach((node) => {
    node.textContent = String(new Date().getFullYear());
  });
})();
