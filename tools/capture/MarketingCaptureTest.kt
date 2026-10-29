package com.example

import androidx.activity.ComponentActivity
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.material3.Scaffold
import androidx.compose.runtime.Composable
import androidx.compose.runtime.mutableStateOf
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.test.junit4.createAndroidComposeRule
import androidx.compose.ui.test.onRoot
import androidx.compose.ui.test.onNodeWithText
import androidx.compose.ui.test.performClick
import com.example.ui.theme.MyApplicationTheme
import com.github.takahirom.roborazzi.captureRoboImage
import org.junit.Rule
import org.junit.Test
import org.junit.runner.RunWith
import org.robolectric.RobolectricTestRunner
import org.robolectric.annotation.Config
import org.robolectric.annotation.GraphicsMode
import java.io.File

/** Controlled sample data, unmodified production composables, Android software renderer. */
@RunWith(RobolectricTestRunner::class)
@GraphicsMode(GraphicsMode.Mode.NATIVE)
@Config(sdk = [35], qualifiers = "w390dp-h844dp-xhdpi")
class MarketingCaptureTest {
  @get:Rule val composeRule = createAndroidComposeRule<ComponentActivity>()

  private val outputDir = File("C:/Dev/PrayerLock/Website/assets/screenshots").apply { mkdirs() }
  private val schedules = listOf(
    PrayerSchedule("Fajr", "5:55 am"),
    PrayerSchedule("Dhuhr", "12:39 pm"),
    PrayerSchedule("Asr", "3:45 pm"),
    PrayerSchedule("Maghrib", "6:17 pm"),
    PrayerSchedule("Isha", "7:32 pm")
  )

  @Composable private fun Frame(prayer: String, tab: Int = 0, content: @Composable () -> Unit) {
    MyApplicationTheme {
      Box(Modifier.fillMaxSize().background(Brush.verticalGradient(getPrayerSkyColors(prayer).skyGradient))) {
        Scaffold(
          containerColor = Color.Transparent,
          bottomBar = { CustomBottomNavigation(selectedTab = tab, onTabSelected = {}) }
        ) { padding ->
          Box(Modifier.fillMaxSize().padding(padding)) { content() }
        }
      }
    }
  }

  private fun captureHome(prayer: String, seconds: Int) {
    composeRule.setContent {
      Frame(prayer) {
        HomeTabScreen(
          currentTimeStr = "5:35", countdownSeconds = seconds, iqamahOffset = 10,
          nextPrayer = prayer, currentPrayer = prayer, isStrict = true,
          isSkipNext = false, isExemption = false, isFocusBlockActive = false,
          focusElapsed = 0, isManualFocus = false, onManualFocusToggle = {},
          weeklyBypassBlocksCount = 0, onWeeklyBypassBlocksClick = {},
          onExemptionToggle = {}, onSkipToggle = {}, onFocusToggle = {},
          prayerSchedules = schedules, onScheduleToggle = {}, onLockMethodToggle = {},
          onOverrideSilentToggle = {}, onCustomVoiceChange = { _, _ -> },
          onTestSoundRequest = { _, _, _ -> },
          locationName = "Lower Swatara Township", sunriseTimeStr = "7:25 am"
        )
      }
    }
    composeRule.waitForIdle()
    composeRule.onRoot().captureRoboImage(File(outputDir, "home-${prayer.lowercase()}.png").absolutePath)
  }

  @Test fun homeFajr() = captureHome("Fajr", 53 * 60)
  @Test fun homeDhuhr() = captureHome("Dhuhr", 114 * 60)
  @Test fun homeAsr() = captureHome("Asr", 90 * 60)
  @Test fun homeMaghrib() = captureHome("Maghrib", 42 * 60)
  @Test fun homeIsha() = captureHome("Isha", 27 * 60)

  @Test fun qibla() {
    composeRule.setContent {
      Frame("Isha", 1) {
        QiblaCompassScreen(false, {}, mutableStateOf("40.1965"), mutableStateOf("-76.7436"), mutableStateOf("Lower Swatara Township"))
      }
    }
    composeRule.waitForIdle()
    composeRule.onRoot().captureRoboImage(File(outputDir, "qibla.png").absolutePath)
  }

  @Test fun adhkar() {
    composeRule.setContent { Frame("Isha", 2) { AdhkarTabScreen("Maghrib") } }
    composeRule.waitForIdle()
    composeRule.onRoot().captureRoboImage(File(outputDir, "adhkar.png").absolutePath)
  }

  @Test fun prayerShield() {
    composeRule.setContent {
      MyApplicationTheme {
        OverlayContent(prayerName = "Maghrib", isCustomFocus = false, isStrict = true, isNfcConfirmationRequired = false, onDismiss = {})
      }
    }
    composeRule.waitForIdle()
    composeRule.onRoot().captureRoboImage(File(outputDir, "prayer-shield.png").absolutePath)
  }

  @Test fun adhkarInteraction() {
    composeRule.setContent { Frame("Isha", 2) { AdhkarTabScreen("Maghrib") } }
    composeRule.waitForIdle()
    composeRule.onRoot().captureRoboImage(File(outputDir, "adhkar-step-00.png").absolutePath)
    composeRule.onNodeWithText("0").performClick()
    composeRule.waitForIdle()
    composeRule.onRoot().captureRoboImage(File(outputDir, "adhkar-step-01.png").absolutePath)
    composeRule.onNodeWithText("1").performClick()
    composeRule.waitForIdle()
    composeRule.onRoot().captureRoboImage(File(outputDir, "adhkar-step-02.png").absolutePath)
    composeRule.onNodeWithText("2").performClick()
    composeRule.mainClock.advanceTimeBy(100)
    composeRule.onRoot().captureRoboImage(File(outputDir, "adhkar-step-03.png").absolutePath)
  }
}
