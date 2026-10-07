<?php
// Приём заявок с лендингов. Настройки — в config.php (см. config.sample.php).
header('Content-Type: application/json; charset=utf-8');
date_default_timezone_set('Europe/Simferopol');

function out($ok, $code = 200) { http_response_code($code); echo json_encode(['ok' => $ok]); exit; }
function h($s) { return htmlspecialchars((string)$s, ENT_NOQUOTES | ENT_SUBSTITUTE, 'UTF-8'); }
function clean($s, $n) { return mb_substr(trim(strip_tags((string)$s)), 0, $n); }

if ($_SERVER['REQUEST_METHOD'] !== 'POST') out(false, 405);

$cfg = @include __DIR__ . '/config.php';
if (!is_array($cfg)) $cfg = [];

$d = json_decode(file_get_contents('php://input'), true);
if (!is_array($d)) $d = $_POST;

// Ловушка для ботов: настоящий человек это поле не видит и не заполняет
if (!empty($d['website'])) out(true);

$phone = trim((string)($d['phone'] ?? ''));
$digits = preg_replace('/\D/', '', $phone);
if (strlen($digits) < 10 || strlen($digits) > 12) out(false, 422);

// Приводим номер к виду 7XXXXXXXXXX и красиво форматируем
$norm = $digits;
if (strlen($norm) === 10) $norm = '7' . $norm;
if (strlen($norm) === 11 && $norm[0] === '8') $norm = '7' . substr($norm, 1);
$pretty = (strlen($norm) === 11 && $norm[0] === '7')
    ? sprintf('+7 (%s) %s-%s-%s', substr($norm, 1, 3), substr($norm, 4, 3), substr($norm, 7, 2), substr($norm, 9, 2))
    : $phone;

$name = clean($d['name'] ?? '', 60);
$comment = clean($d['comment'] ?? '', 400);
$page = mb_substr(preg_replace('/[^a-z0-9\-\/]/i', '', (string)($d['page'] ?? '')), 0, 60);
$search = mb_substr((string)($d['search'] ?? ''), 0, 200);
$ref = clean($d['ref'] ?? '', 200);

// Не чаще одной заявки в 20 секунд с одного адреса
$ip = $_SERVER['REMOTE_ADDR'] ?? '0';
$lock = sys_get_temp_dir() . '/lead_' . md5($ip);
if (is_file($lock) && time() - filemtime($lock) < 20) out(false, 429);
@touch($lock);

// Названия страниц для читаемого сообщения
$titles = [
    'resanta' => 'Стабилизатор Ресанта', '10kvt' => 'Стабилизатор для дома 10 кВт', 'spn-13500' => 'Ресанта СПН-13500',
    'exegate' => 'Exegate для дома', 'exegate-15kvt' => 'Exegate 15 кВт',
    'spn-13500-wow' => 'Ресанта СПН-13500 (анимация)', 'exegate-15kvt-wow' => 'Exegate 15 кВт (анимация)',
    '10kvt-beacon' => '10 кВт (Beacon)', 'exegate-warm' => 'Exegate для дома (Coffee)', 'resanta-cinnabar' => 'Ресанта (Cinnabar)',
];
$slug = trim($page, '/');
$title = $titles[$slug] ?? ($slug !== '' ? $slug : 'Главная');
$tag = '#' . str_replace('-', '_', preg_replace('/[^a-z0-9\-]/i', '', $slug !== '' ? $slug : 'home'));

// Метки рекламы из адресной строки
parse_str(ltrim($search, '?'), $q);
$src = [];
foreach (['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content'] as $k) {
    if (!empty($q[$k])) $src[] = clean($q[$k], 60);
}
$yclid = !empty($q['yclid']) ? clean($q['yclid'], 40) : '';
$source = $src ? implode(' / ', $src) : ($yclid !== '' ? 'Яндекс Директ' : ($ref !== '' ? parse_url($ref, PHP_URL_HOST) : 'прямой заход'));

$ua = $_SERVER['HTTP_USER_AGENT'] ?? '';
$device = preg_match('/Mobile|Android|iPhone|iPad/i', $ua) ? '📱 Телефон' : '🖥 Компьютер';

$when = date('d.m.Y H:i');
$pageUrl = 'https://oasis.com.ru' . ($page !== '' ? $page : '/');

// --- сообщение для Telegram (HTML) ---
$m  = "🔔 <b>Новая заявка</b>\n";
$m .= "━━━━━━━━━━━━━━━\n";
$m .= "👤 <b>Имя:</b> " . ($name !== '' ? h($name) : '<i>не указано</i>') . "\n";
$m .= "📞 <b>Телефон:</b> " . h($pretty) . "\n";
$m .= "📋 <code>+" . h($norm) . "</code> <i>(нажмите, чтобы скопировать для MAX)</i>\n";
if ($comment !== '') $m .= "\n💬 <b>Комментарий</b>\n<blockquote>" . h($comment) . "</blockquote>\n";
$m .= "━━━━━━━━━━━━━━━\n";
$m .= "📄 <b>Страница:</b> " . h($title) . "\n";
$m .= "🎯 <b>Источник:</b> " . h($source) . "\n";
if ($yclid !== '') $m .= "🔗 <b>yclid:</b> <code>" . h($yclid) . "</code>\n";
$m .= "$device · 🕐 $when\n\n";
$m .= "#заявка $tag";

// Кнопки под сообщением
$buttons = [[]];
if (strlen($norm) === 11) {
    // У MAX нет ссылки на чат по номеру: открываем веб-версию, номер вставляется в поиск
    $buttons[0][] = ['text' => '💬 MAX', 'url' => 'https://web.max.ru/'];
    $buttons[0][] = ['text' => '✈️ Telegram', 'url' => 'https://t.me/+' . $norm];
}
$buttons[] = [['text' => '🌐 Открыть страницу', 'url' => $pageUrl]];
$markup = json_encode(['inline_keyboard' => $buttons], JSON_UNESCAPED_UNICODE);

// --- простой текст для почты ---
$plain = "Новая заявка\nИмя: " . ($name ?: '-') . "\nТелефон: $pretty\n"
       . ($comment !== '' ? "Комментарий: $comment\n" : '')
       . "Страница: $title\nИсточник: $source\nВремя: $when";

$sent = false;

if (!empty($cfg['tg_token']) && !empty($cfg['tg_chat_id'])) {
    $url = 'https://api.telegram.org/bot' . $cfg['tg_token'] . '/sendMessage';
    $post = http_build_query([
        'chat_id' => $cfg['tg_chat_id'], 'text' => $m, 'parse_mode' => 'HTML',
        'disable_web_page_preview' => 'true', 'reply_markup' => $markup,
    ]);
    $res = false; $code = 0;
    if (function_exists('curl_init')) {
        $ch = curl_init($url);
        curl_setopt_array($ch, [CURLOPT_POST => true, CURLOPT_POSTFIELDS => $post,
            CURLOPT_RETURNTRANSFER => true, CURLOPT_TIMEOUT => 8]);
        $res = curl_exec($ch);
        $code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        curl_close($ch);
    } else {
        $ctx = stream_context_create(['http' => ['method' => 'POST', 'timeout' => 8, 'ignore_errors' => true,
            'header' => "Content-Type: application/x-www-form-urlencoded\r\n", 'content' => $post]]);
        $res = @file_get_contents($url, false, $ctx);
        $code = $res !== false ? 200 : 0;
    }
    if ($res !== false && $code === 200) {
        $sent = true;
    } else {
        @file_put_contents(sys_get_temp_dir() . '/tg_err.log', date('c') . ' ' . $code . ' ' . substr((string)$res, 0, 300) . "\n", FILE_APPEND);
        // Запасной вариант: если Telegram отклонил разметку, шлём простым текстом
        $post2 = http_build_query(['chat_id' => $cfg['tg_chat_id'], 'text' => $plain, 'reply_markup' => $markup]);
        if (function_exists('curl_init')) {
            $ch = curl_init($url);
            curl_setopt_array($ch, [CURLOPT_POST => true, CURLOPT_POSTFIELDS => $post2,
                CURLOPT_RETURNTRANSFER => true, CURLOPT_TIMEOUT => 8]);
            $r2 = curl_exec($ch); $c2 = curl_getinfo($ch, CURLINFO_HTTP_CODE); curl_close($ch);
            if ($r2 !== false && $c2 === 200) $sent = true;
        }
    }
}

if (!empty($cfg['email'])) {
    $headers = "Content-Type: text/plain; charset=utf-8\r\n";
    if (@mail($cfg['email'], '=?UTF-8?B?' . base64_encode('Новая заявка на стабилизатор') . '?=', $plain, $headers)) $sent = true;
}

out($sent, $sent ? 200 : 500);
