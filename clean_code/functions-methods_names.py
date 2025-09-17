'''
Задание 5

Улучшение имен функций/методов

1. handleFirmData - setFirmName  (метод получает имя компании и ставит его в форму)


2. validate - validateFormFields  (метод валидации всех полей формы)


3. getRequestObject - getDocumentFields  (метод, создающий объект со всеми полями, необходимыми
для создания нового документа)


4. signerPopupAction - saveCredentials  (метод, сохраняющий новые данные подписанта)


5. openSignerPopup - setCurrentCertAndUser
    (метод сохраняет данные текущего пользователя и его сертификата при открытии попапа. Само открытие вынесено в
    отдельный метод)


6. getRequisitesFromBackend - getRequisitesAndSetDocState
    (метод получения реквизитов и добавления их в стэйт документа.
    Ясно, что этот метод не должен работать с состоянием, но код старый, пока не могу это переписать)


7. getDataToSave - constructDocBody
    (метод собирает в один объект все поля, необходимые для создания документа)


8. loadDocument - previewDocument
    (метод, открывающий документ для превью)


9. needToShowBillingPopup - isShowBillingPopup
    (метод, определяющий показывать или нет попап биллинга)


10. setDocTemplateNameHandler - setDocTemplateName
    (метод, задающий имя для шаблона документа)


11. approvedByUser - isDocApprovedByUser
    (метод, проверяющий одобрен ли документ пользователем)


12. defineFixPriceText - buildFixPriceText
    (метод, строящий строку информации при фиксированной цене
    и в зависимости от наличия флагов в документе)

'''